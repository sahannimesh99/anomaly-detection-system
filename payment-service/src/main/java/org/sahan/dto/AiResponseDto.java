package org.sahan.dto;

import lombok.Data;

@Data
public class AiResponseDto {
    private boolean anomaly;
    private double score;
    private String severity;
    private String anomaly_type;
    private double model_score;
    private double rule_score;
    private String model_prediction;
}
