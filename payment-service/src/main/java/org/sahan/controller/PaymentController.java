package org.sahan.controller;

import lombok.RequiredArgsConstructor;
import org.sahan.dto.PagedResponseDto;
import org.sahan.dto.PaymentDto;
import org.sahan.service.PaymentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/payments")
@RequiredArgsConstructor
@CrossOrigin(origins = "*")
@ControllerAdvice
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
}