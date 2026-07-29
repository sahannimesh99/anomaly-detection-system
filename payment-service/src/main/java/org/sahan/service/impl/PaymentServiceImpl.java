package org.sahan.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ModelMapper;
import org.sahan.dto.AiRequestDto;
import org.sahan.dto.AiResponseDto;
import org.sahan.dto.PagedResponseDto;
import org.sahan.dto.PaymentDto;
import org.sahan.entity.Payment;
import org.sahan.repository.PaymentRepository;
import org.sahan.service.PaymentService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Random;

@Service
@RequiredArgsConstructor
@Slf4j
public class PaymentServiceImpl implements PaymentService {

    private final PaymentRepository paymentRepository;
    private final ModelMapper modelMapper;
    private final Random random = new Random();
    private final RestTemplate restTemplate;

    @Value("${ai.service.url:http://localhost:5000/detect}")
    private String aiServiceUrl;

    public PaymentDto process(PaymentDto dto) {
        log.info("Processing payment for orderId: {}", dto.getOrderId());

        boolean isFailure = random.nextInt(10) < 3;

        Payment payment = new Payment();
        payment.setOrderId(dto.getOrderId());
        payment.setAmount(dto.getAmount());

        String status = isFailure ? "FAILED" : "SUCCESS";
        payment.setStatus(status);

        if (isFailure) {
            log.error("Payment FAILED for orderId: {}", dto.getOrderId());
        } else {
            log.info("Payment SUCCESS for orderId: {}", dto.getOrderId());
        }

        AiRequestDto aiRequest = AiRequestDto.builder()
                .amount(dto.getAmount())
                .status(status)
                .error_count(isFailure ? 3 : 0)
                .request_count(50)
                .response_time_ms(isFailure ? 800.0 : 120.0)
                .build();

        try {
            AiResponseDto aiResponse = restTemplate.postForObject(
                    aiServiceUrl,
                    aiRequest,
                    AiResponseDto.class
            );

            log.info("AI Response: {}", aiResponse);

            if (aiResponse != null) {
                payment.setAnomaly(aiResponse.isAnomaly());
                payment.setAnomalyType(aiResponse.getAnomaly_type());
                payment.setSeverity(aiResponse.getSeverity());

                if (aiResponse.isAnomaly()) {
                    log.warn("ANOMALY DETECTED - Type: {}, Severity: {}",
                            aiResponse.getAnomaly_type(),
                            aiResponse.getSeverity());
                }
            }
        } catch (Exception e) {
            log.error("AI service call failed (Payment Service): {}", e.getMessage());
            payment.setAnomaly(false);
            payment.setAnomalyType("NORMAL");
            payment.setSeverity("LOW");
        }

        Payment saved = paymentRepository.save(payment);
        return modelMapper.map(saved, PaymentDto.class);
    }

    public PaymentDto getById(Long id) {
        log.info("Fetching payment by id: {}", id);
        Payment payment = paymentRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Payment not found with id: " + id));
        return modelMapper.map(payment, PaymentDto.class);
    }

    public List<PaymentDto> getByOrderId(Long orderId) {
        log.info("Fetching payments by orderId: {}", orderId);
        return paymentRepository.findByOrderId(orderId)
                .stream()
                .map(payment -> modelMapper.map(payment, PaymentDto.class))
                .toList();
    }

    public List<PaymentDto> getAll() {
        log.info("Fetching all payments");
        return paymentRepository.findAll()
                .stream()
                .map(payment -> modelMapper.map(payment, PaymentDto.class))
                .toList();
    }

    public PagedResponseDto<PaymentDto> getAll(int page, int size, String filter) {
        log.info("Fetching payments - page: {}, size: {}, filter: {}", page, size, filter);

        PageRequest pageable = PageRequest.of(page, size, Sort.by(Sort.Direction.DESC, "id"));

        Page<Payment> pagedResult = switch (filter == null ? "all" : filter.toLowerCase()) {
            case "anomalies" -> paymentRepository.findByAnomalyTrue(pageable);
            case "critical"  -> paymentRepository.findBySeverity("CRITICAL", pageable);
            case "safe"      -> paymentRepository.findByAnomalyFalse(pageable);
            default          -> paymentRepository.findAll(pageable);
        };

        List<PaymentDto> content = pagedResult.getContent()
                .stream()
                .map(payment -> modelMapper.map(payment, PaymentDto.class))
                .toList();

        return PagedResponseDto.<PaymentDto>builder()
                .content(content)
                .page(pagedResult.getNumber())
                .size(pagedResult.getSize())
                .totalElements(pagedResult.getTotalElements())
                .totalPages(pagedResult.getTotalPages())
                .last(pagedResult.isLast())
                .build();
    }
}
