package org.sahan.service;

import org.sahan.dto.PagedResponseDto;
import org.sahan.dto.PaymentDto;

import java.util.List;

public interface PaymentService {
    PaymentDto process(PaymentDto user);
    List<PaymentDto> getAll();
    PagedResponseDto<PaymentDto> getAll(int page, int size, String filter);
}
