package org.sahan.service;

import org.sahan.dto.OrderDto;

import java.util.List;

public interface OrderService {
    String save(OrderDto dto);
    OrderDto update(Long id, OrderDto dto);
    OrderDto getById(Long id);
    List<OrderDto> getByUserId(Long userId);
    void delete(Long id);
    List<OrderDto> getAll();
}
