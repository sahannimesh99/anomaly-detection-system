package org.sahan.service;

import org.sahan.dto.UserDto;
import org.sahan.entity.User;

import java.util.List;

public interface UserService {
    String save(UserDto user);
    List<UserDto> getAll();
}
