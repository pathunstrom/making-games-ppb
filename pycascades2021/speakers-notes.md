1. Introduction - no more than 4 minutes
    1. Welcome
    2. Who Am I?
        - Me
        - Position
        - Open Source
    3. This Talk
        1. Introduction to the building blocks of ppb
        2. Goals:
            - By the end, you should feel comfortable experimenting on your own game
            - How to think about game creation
            - Understanding Events and the event loop
            - The purpose of and use of Scenes
            - Whats the difference between Sprites and GameObjects
2. Getting Started
    1. Why ppb?
        - elevator pitch about education focus
        - key benefits for a dev focused audience
            - Easy to get started
            - It lets you solve the problems you care about
            - Deeply extensible
    2. So how fast can you get started?
        - ppb.run()
        - keyword arguments that matter here: setup and starting_scene
            - setup is a callable that accepts a ppb Scene
                - think of it like an init function!
            - starting_scene is the class that is instantiated before passed to setup
            - This flexibility allows you to progressively grow the complexity of your initialization.
3. Sprites and Events:
    1. Sprites
        - visible game objects
        - Can take arbitrary keyword arguments
        - Rendered
            - use the image attribute to change their look
            - rendered centered on their position attribute
            - used sprite.rotation to rotate the image
            - uses the sprite's dimensions to determine their size
        - Making them move using events
        - The shape of an event handler
    2. Events
        1. What are events?
            * A thing happened, or should happen
            * A brief list of ppb defined events
        2. Defining events
            - Simple classes
                - must have a globally unique name
                - best practice is classes should only hold data
            - dataclasses!
        3. Emitting events
            - Signal function
            - parameters are an event instance and targets
            - Good for communication between game objects!
4. Scenes and GameObjects:
    1. So let's swap from a setup function to a scene
    2. What are Scenes?
        - Conceptually "parts" of a game
        - If the layout of a section is significantly different
            - menus, credits, different levels
        - Containers
    3. How you should use them
        - Every menu, splash screen, or level of your game is its own scene
        - Don't worry about reused code for your first game or six.
        - Going between scenes
            - Scenes stored in a stack
            - Starts with your first scene
            - Emit a StartScene to add a new scene to the stack
            - ReplaceScene let's you pop the current scene and start a new one
                - To pass arguments, use the args and kwargs attributes on these scenes
            - use StopScene to pop a scene from the stack.
        - Clever use of the scene stack allows all kinds of trick, like failing out to a splash screen before restarting.
        - Besides these events, there are life cycle events that allow other objects to know when scenes start, stop, pause and continue.
    4. GameObjects
        - Absolutely everything we've discussed so far is a game object, even the engine.
        - They create an object graph or tree that can be walked by the game engine to publish events at any level.
        - Good for when you don't need all the features of a Sprite, but still want a separate object in your scene.
            - Things like scoring systems or npc controllers.
5. Systems (Very quick)
    - exercise of the watcher
    - context managers
        - good for setting up and tearing down non-game resources (like hardware libraries or networked resources)
    - Also game objects
        - can have children objects
        - respond to events
        - Most systems listen for their own communication events or the Idle heartbeat event.
6. The end
    1. Tips
        1. games are complex!
        2. Start simple!
        3. Work on one thing at a time until it works, then add more features.
        4. There are multiple ways to solve problems in game development, don't worry about getting it wrong
        5. Games risk ending up with tightly coupled logic, use composition and abstract classes to support type hinting
    2. Summary
        1. ppb games building blocks
            1. Sprites
            2. Scenes
            3. Events
        2. ppb supports progressive complexity
            1. Start with a setup function and a player sprite
            2. move to scenes when you need event handlers, more complex setup, or more than one scene
            3. Explore systems when you need code  that runs across multiple scenes
        3. Learn more
            1. twitch.tv/pathunstrom
            2. @pathunstrom
            3. ppb.dev (join our discord!)
            4. ppb.readthedocs.io