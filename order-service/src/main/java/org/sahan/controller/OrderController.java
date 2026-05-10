package org.sahan.controller;

import lombok.RequiredArgsConstructor;

import org.sahan.dto.OrderDto;
import org.sahan.service.OrderService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/orders")
@RequiredArgsConstructor
@CrossOrigin(origins = "*")
@ControllerAdvice
public class OrderController {

    private final OrderService orderService;

    @PostMapping
    public ResponseEntity<String> create(@RequestBody OrderDto dto) {
        return ResponseEntity.ok(orderService.save(dto));
    }

    @GetMapping
    public List<OrderDto> getAll() {
        return orderService.getAll();
    }
}