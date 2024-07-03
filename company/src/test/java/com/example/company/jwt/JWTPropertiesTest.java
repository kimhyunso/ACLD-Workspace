package com.example.company.jwt;

import com.example.company.domain.JwtProperties;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

@SpringBootTest
class JWTPropertiesTest {
    @Autowired
    private JwtProperties jwtProperties;

    @Test
    void jwt_설정값_불러오기_성공_테스트() {
        // given
        // when
        System.out.println("jwtProperties.getIssuer() = " + jwtProperties.getIssuer());
        System.out.println("jwtProperties.getSecretKey() = " + jwtProperties.getSecretKey());

        // then
        assertThat(jwtProperties.getSecretKey())
                .isNotNull();


        assertThat(jwtProperties.getIssuer())
                .isNotNull();
    }
}