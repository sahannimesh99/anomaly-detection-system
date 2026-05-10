package org.sahan.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ModelMapper;
import org.sahan.common.AiClient;
import org.sahan.dto.AiRequestDto;
import org.sahan.dto.AiResponseDto;
import org.sahan.dto.OrderDto;
import org.sahan.entity.Order;
import org.sahan.repository.OrderRepository;
import org.sahan.service.OrderService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class OrderServiceImpl implements OrderService {

    private final OrderRepository orderRepository;
    private final ModelMapper modelMapper;
    private final AiClient aiClient;

    public String save(OrderDto dto) {

        log.info("Creating order for userId: {}", dto.getUserId());

        if (dto.getAmount() > 10000) {
            log.warn("High value order detected: {}", dto.getAmount());
        }

        Order order = modelMapper.map(dto, Order.class);

        AiRequestDto aiRequest = AiRequestDto.builder()
                .amount(dto.getAmount())
                .status("SUCCESS")
                .error_count(0)
                .request_count(60)
                .response_time_ms(200.0)
                .build();

        AiResponseDto aiResponse = aiClient.detect(aiRequest);

        log.info("AI Response: {}", aiResponse);

        if (aiResponse != null) {

            order.setAnomaly(aiResponse.isAnomaly());
            order.setAnomalyType(aiResponse.getAnomaly_type());
            order.setSeverity(aiResponse.getSeverity());

            if (aiResponse.isAnomaly()) {
                log.warn("🔥 ORDER ANOMALY DETECTED → Type: {}, Severity: {}",
                        aiResponse.getAnomaly_type(),
                        aiResponse.getSeverity());
            }
        }

        Order saved = orderRepository.save(order);

        log.info("Order saved with id: {}", saved.getId());

        return "Saved Successfully";
    }

    public List<OrderDto> getAll() {
        return orderRepository.findAll()
                .stream()
                .map(order -> modelMapper.map(order, OrderDto.class))
                .toList();
    }

}
