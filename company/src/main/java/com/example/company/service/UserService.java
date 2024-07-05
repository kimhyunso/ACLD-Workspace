package com.example.company.service;

import com.example.company.domain.User;
import com.example.company.domain.UserRole;
import com.example.company.dto.RequestUser;
import com.example.company.repository.UserRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public User save(RequestUser requestUser){
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
        User addUser = createUser(requestUser, encoder);
        return userRepository.save(addUser);
    }

    private User createUser(RequestUser requestUser, BCryptPasswordEncoder encoder) {
        return User.builder()
                .email(requestUser.getEmail())
                .password(encoder.encode(requestUser.getPassword()))
                .userRole(UserRole.USER).build();
    }

    public User findByEmail(String email){
        return userRepository.findByEmail(email)
                .orElseThrow(() -> new IllegalArgumentException("잘 못된 이메일입니다."));
    }


}
