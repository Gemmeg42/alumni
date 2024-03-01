package ru.nick.app.repo;

import org.springframework.data.repository.CrudRepository;
import ru.nick.app.model.Alumni;

public interface AlumniRepo extends CrudRepository<String, Alumni> {
}
