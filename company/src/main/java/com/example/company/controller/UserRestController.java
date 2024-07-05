package com.example.company.controller;


import com.example.company.dto.RequestUser;
import com.example.company.service.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@Tag(name = "Example", description = "Example API")
public class UserRestController {

    private final UserService userService;

    @PostMapping("/signup")
    @Operation(summary = "Example API Summary", description = "Your description")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Success",
                    content = {@Content(schema = @Schema(implementation = RequestUser.class))}),
            @ApiResponse(responseCode = "404", description = "Not Found"),
    })
    public String signup(RequestUser request){
        userService.save(request);
        return "redirect:/login";
    }

}
