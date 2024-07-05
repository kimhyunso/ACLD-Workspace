package com.example.company.service;

import com.example.company.domain.RefreshToken;
import com.example.company.domain.User;
import com.example.company.dto.RequestUser;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.Duration;

@Service
@RequiredArgsConstructor
public class TokenService {

    private final TokenProvider tokenProvider;
    private final UserService userService;
    private final RefreshTokenService refreshTokenService;
    private static final int TOKEN_HOURS = 2;

    public String createAccessToken(String refreshToken) throws IllegalArgumentException {
        if (!tokenProvider.validToken(refreshToken)) {
            throw new IllegalArgumentException("잘 못된 토큰 값입니다.");
        }

        String findEmail = refreshTokenService.findByRefreshToken(refreshToken).getEmail();
        User user = userService.findByEmail(findEmail);
        return tokenProvider.generateToken(user, Duration.ofHours(TOKEN_HOURS));
    }

}
