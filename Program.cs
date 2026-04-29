using App.Models;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// In-memory store
var people = new List<Person>();
var nextId = 1;

// GET /pessoas - lista todos
app.MapGet("/pessoas", () => Results.Ok(people));

// GET /pessoas/{id} - busca por id
app.MapGet("/pessoas/{id:int}", (int id) =>
{
    var person = people.FirstOrDefault(p => p.Id == id);
    return person is not null ? Results.Ok(person) : Results.NotFound(new { message = "Pessoa não encontrada." });
});

// POST /pessoas - cria novo
app.MapPost("/pessoas", (Person input) =>
{
    var person = new Person
    {
        Id = nextId++,
        Nome = input.Nome,
        Idade = input.Idade
    };
    people.Add(person);
    return Results.Created($"/pessoas/{person.Id}", person);
});

// PUT /pessoas/{id} - atualiza
app.MapPut("/pessoas/{id:int}", (int id, Person input) =>
{
    var person = people.FirstOrDefault(p => p.Id == id);
    if (person is null)
        return Results.NotFound(new { message = "Pessoa não encontrada." });

    person.Nome = input.Nome;
    person.Idade = input.Idade;
    return Results.Ok(person);
});

// DELETE /pessoas/{id} - remove
app.MapDelete("/pessoas/{id:int}", (int id) =>
{
    var person = people.FirstOrDefault(p => p.Id == id);
    if (person is null)
        return Results.NotFound(new { message = "Pessoa não encontrada." });

    people.Remove(person);
    return Results.NoContent();
});

app.Run();
