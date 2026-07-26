package org.sahan.service;

import org.sahan.dto.UserDto;

import java.util.List;

public interface UserService {
    String save(UserDto user);
    UserDto update(Long id, UserDto user);
    UserDto getById(Long id);
    void delete(Long id);
    List<UserDto> getAll();
}
