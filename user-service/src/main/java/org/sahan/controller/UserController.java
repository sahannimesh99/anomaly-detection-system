package org.sahan.controller;

import lombok.RequiredArgsConstructor;
import org.sahan.dto.UserDto;
import org.sahan.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
@CrossOrigin(origins = "*")
@ControllerAdvice
public class UserController {

    private final UserService userService;

    @PostMapping
    public String create(@RequestBody UserDto user) {
        return userService.save(user);
    }

    @GetMapping
    public List<UserDto> getAll() {
        return userService.getAll();
    }
}