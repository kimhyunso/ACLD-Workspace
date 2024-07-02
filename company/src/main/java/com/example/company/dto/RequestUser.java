package com.example.company.dto;

import com.example.company.domain.UserRole;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class RequestUser {

    private String email;
    private String password;
    private UserRole userRole;

}
