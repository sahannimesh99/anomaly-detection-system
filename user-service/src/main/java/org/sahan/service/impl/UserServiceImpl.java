package org.sahan.service.impl;

import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ModelMapper;
import org.sahan.common.AiClient;
import org.sahan.dto.AiRequestDto;
import org.sahan.dto.AiResponseDto;
import org.sahan.dto.UserDto;
import org.sahan.entity.User;
import org.sahan.repository.UserRepository;
import org.sahan.service.UserService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
@Transactional
@Slf4j
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final ModelMapper modelMapper;
    private final AiClient aiClient;

    private int userCreationCount = 0;

    public String save(UserDto dto) {

        log.info("Creating user with email: {}", dto.getEmail());

        User user = modelMapper.map(dto, User.class);
        User saved = userRepository.save(user);

        log.info("User created with id: {}", saved.getId());

        userCreationCount++;

        if (userCreationCount >= 10) {

            log.warn("High user registration spike detected: {}", userCreationCount);

            AiRequestDto aiRequest = AiRequestDto.builder()
                    .amount(0.0)
                    .status("SUCCESS")
                    .error_count(0)
                    .request_count(userCreationCount)
                    .response_time_ms(100.0)
                    .build();

            try {
                AiResponseDto aiResponse = aiClient.detect(aiRequest);

                log.info("AI Response (User Service): {}", aiResponse);

                if (aiResponse != null && aiResponse.isAnomaly()) {
                    log.warn(" USER ANOMALY DETECTED → Type: {}, Severity: {}",
                            aiResponse.getAnomaly_type(),
                            aiResponse.getSeverity());
                }

            } catch (Exception e) {
                log.error("AI service call failed (User Service): {}", e.getMessage());
            }
            userCreationCount = 0;
        }
        return "Saved Successfully";
    }

    public List<UserDto> getAll() {
        log.info("Fetching all users");
        return userRepository.findAll()
                .stream()
                .map(user -> modelMapper.map(user, UserDto.class))
                .toList();
    }

}
