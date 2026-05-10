package org.sahan.service;

import org.sahan.dto.OrderDto;

import java.util.List;

public interface OrderService {
    String save(OrderDto dto);

    List<OrderDto> getAll();
}
