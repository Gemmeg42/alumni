package ru.nick.app.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import ru.nick.app.model.Alumni;
import ru.nick.app.service.AlumniService;

@Slf4j
@RestController
public class AlumniController {
    private AlumniService alumniService;

    public AlumniController(AlumniService alumniService){
        this.alumniService = alumniService;
    }
    @PostMapping("ex-1/alumni")
    public Alumni create(@RequestBody Alumni data){
        log.info("Data:{}",data.toString());
        return alumniService.create(data);
    }
}
