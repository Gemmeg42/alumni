package ru.nick.app.service;

import org.springframework.stereotype.Service;
import ru.nick.app.model.Alumni;
import ru.nick.app.repo.AlumniRepo;

@Service
public class AlumniService {
    private AlumniRepo alumniRepo;

    public AlumniService(AlumniRepo alumniRepo) {
        this.alumniRepo = alumniRepo;
    }

    public Alumni create(Alumni data){
        return alumniRepo.save(data);
    }
}
