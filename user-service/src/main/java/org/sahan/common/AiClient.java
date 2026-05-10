package org.sahan.common;

import lombok.RequiredArgsConstructor;
import org.sahan.dto.AiRequestDto;
import org.sahan.dto.AiResponseDto;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
@RequiredArgsConstructor
public class AiClient {

    private final RestTemplate restTemplate;

    public AiResponseDto detect(AiRequestDto request) {
        try {
            return restTemplate.postForObject(
                    "http://localhost:5000/detect",
                    request,
                    AiResponseDto.class
            );
        } catch (Exception e) {
            return null;
        }
    }
}