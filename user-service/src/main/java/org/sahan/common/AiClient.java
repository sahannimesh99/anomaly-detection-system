package org.sahan.common;

import lombok.RequiredArgsConstructor;
import org.sahan.dto.AiRequestDto;
import org.sahan.dto.AiResponseDto;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
@RequiredArgsConstructor
public class AiClient {

    private final RestTemplate restTemplate;

    @Value("${ai.service.url:http://localhost:5000/detect}")
    private String aiServiceUrl;

    public AiResponseDto detect(AiRequestDto request) {
        try {
            return restTemplate.postForObject(
                    aiServiceUrl,
                    request,
                    AiResponseDto.class
            );
        } catch (Exception e) {
            return null;
        }
    }
}