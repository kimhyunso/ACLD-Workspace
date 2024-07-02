package com.example.company.repository;

import com.example.company.domain.User;
import com.example.company.domain.key.UserKey;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, UserKey>{

    Optional<User> findByEmail(String email);

}
