package org.sahan.dto;

import lombok.Data;

@Data
public class PaymentDto {
    private Long id;
    private Long orderId;
    private Double amount;
    private String status;
    private Boolean anomaly;
    private String anomalyType;
    private String severity;
}
