package com.example.company.dto;

import com.example.company.domain.UserRole;
import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class RequestUser {

    private String email;
    private String password;

}
