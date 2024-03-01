package ru.nick.app.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "alumni")
public class Alumni {

    @Id
    public String id;
    public String name;
}
