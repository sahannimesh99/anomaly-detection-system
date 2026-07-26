package org.sahan.controller;

import lombok.RequiredArgsConstructor;
import org.sahan.dto.PagedResponseDto;
import org.sahan.dto.PaymentDto;
import org.sahan.service.PaymentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping({"/api/payments", "/payments"})
@RequiredArgsConstructor
public class PaymentController {

    private final PaymentService paymentService;

    @PostMapping
    public ResponseEntity<PaymentDto> process(@RequestBody PaymentDto dto) {
        return ResponseEntity.ok(paymentService.process(dto));
    }

    @GetMapping
    public ResponseEntity<PagedResponseDto<PaymentDto>> getAll(
            @RequestParam(defaultValue = "0")   int    page,
            @RequestParam(defaultValue = "10")  int    size,
            @RequestParam(defaultValue = "all") String filter) {
        return ResponseEntity.ok(paymentService.getAll(page, size, filter));
    }

    @GetMapping("/{id}")
    public ResponseEntity<PaymentDto> getById(@PathVariable Long id) {
        return ResponseEntity.ok(paymentService.getById(id));
    }

    @GetMapping("/order/{orderId}")
    public ResponseEntity<List<PaymentDto>> getByOrderId(@PathVariable Long orderId) {
        return ResponseEntity.ok(paymentService.getByOrderId(orderId));
    }
}