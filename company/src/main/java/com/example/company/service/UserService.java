package com.example.company.service;

import com.example.company.domain.User;
import com.example.company.domain.UserRole;
import com.example.company.dto.RequestUser;
import com.example.company.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public Long save(RequestUser requestUser){
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
        User addUser = createUser(requestUser, encoder);
        return userRepository.save(addUser).getUserNo();
    }

    private User createUser(RequestUser requestUser, BCryptPasswordEncoder encoder){
        return User.builder()
                .email(requestUser.getEmail())
                .password(encoder.encode(requestUser.getPassword()))
                .userRole(UserRole.USER).build();
    }



}
