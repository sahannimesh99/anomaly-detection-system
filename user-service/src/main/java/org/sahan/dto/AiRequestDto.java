package org.sahan.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AiRequestDto {
    private Double amount;
    private String status;
    private Integer error_count;
    private Integer request_count;
    private Double response_time_ms;
}