# pythfinder-cli spec
Defines the spec for the client application.

## Syntax
pythfinder-cli \<action> \<collection> \<filter> \<values> \<target>

### Action
Several CRUD operations and other specific actions are supported:

* get
* create
* update
* delete
* copy

### Collection
Can be either "character" for the whole character sheet, or one of the 
existing collection properties (all also accept singular nouns):

* abilities
* classes
* saving throws (abbreviated to "saves" or "throws")
* feats/traits/specials
* equipment (accepts "item(s)")
* skills
* spells
* attacks
* armor

### Filter
Can take multiple forms:

* If a collection is specified, a plain uuid can be provided to specify 
  one particular item.
* If trying to get multiple collection items, filters can be specified 
  as JSON, e.g.:
```
pythfinder-cli get equipment '{"weight": {"ge": 4, "le": 6}, "location": ["backpack", "belt"]}' pythfinder.io/00000000-0000-0000-0000-000000000000
```

### Values
New values for create/update actions. Accepts a JSON string

### Target
The target character sheet. Plans to support file, scp, and 
pythfinder.io targets, e.g.:

* path/to/file.json
* scp://user@server.com:/path/to/file.json
* pythfinder.io/\<uuid>
