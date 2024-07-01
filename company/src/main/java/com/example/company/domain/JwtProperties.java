package com.example.company.domain;

import io.jsonwebtoken.SignatureAlgorithm;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

import javax.crypto.spec.SecretKeySpec;
import java.security.Key;

@ConfigurationProperties("app.jwt")
@Builder
@Getter
@Setter
public class JwtProperties {
    private String issuer;
    private String secretKey;
    private Long expired;


}
