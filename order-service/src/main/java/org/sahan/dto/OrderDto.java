package org.sahan.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class OrderDto {
    private Long userId;
    private String product;
    private Double amount;
    private Boolean anomaly;
    private String anomalyType;
    private String severity;
}
