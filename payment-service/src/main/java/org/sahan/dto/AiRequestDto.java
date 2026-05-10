package org.sahan.dto;

import lombok.*;

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