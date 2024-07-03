CREATE TABLE users (
    user_no BIGINT NOT NULL GENERATED BY DEFAULT AS IDENTITY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    user_role VARCHAR(255) NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY (user_no, email)
);