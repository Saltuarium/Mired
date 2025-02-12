# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Testing


define a = Character('Alys', image='alys', callback=name_callback, cb_name='Al')
define t = Character('Tierney', image='tierney', callback=name_callback, cb_name='Tier')
define m = Character('Man', image='man', callback=name_callback, cb_name='man')
define narrator = Character(callback=name_callback, cb_name=None)
define nvl_narr = Character(None, kind=nvl)

default humanity = 0

define config.speaking_attribute = "talking"

init python:
    renpy.music.register_channel("music2", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("ambient", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)


    def cf(track_new, track_new_loop=None, curr_time=4.2,new_time=4.2):
        curr_track = "music"
        x_fade_track = "music2"
        do_loop = True
        if track_new_loop is not None:
            do_loop = False
        if not renpy.music.is_playing("music"):
            x_fade_track = "music"
            curr_track = "music2"
        renpy.music.stop(curr_track,fadeout=curr_time)
        renpy.music.play(track_new,channel=x_fade_track,fadein=new_time,loop=do_loop)
        if not do_loop:
            renpy.music.queue(track_new_loop,channel=x_fade_track,loop=True)

transform rightish:
    xalign 0.85
    yalign 1.0

transform leftish: 
    xalign 0.15 
    yalign 1.0

# The game starts here.

label start:

    show bg lake
    play ambient "Daytime Ambience.ogg" fadeout 1.0 fadein 1.0
    "When I wake in the fen, there is a long moment in which the pain in my leg is all I can consider. I am aware of it before I am aware of myself."
    "I try to ease myself to a sitting position without disturbing my wound, wincing anyway as the movement sets it to throbbing again."
    "Looking at it, it's immediately apparent that the bandages need changing. I can feel a heat coming off of the gash as I gingerly reach towards it, before turning and examining my surroundings."
    "When I woke yesterday, I was alone. I had stumbled as if in a daze, sweating despite the chill and too tired to swat away the biting midges."
    "I recall seeing a strange blue light - a torch in the distance? - and following it to what I believed was a figure before finally collapsing."
    "If I met someone before, they're not here now. Around me are only the long grasses and pooling water of the wetlands."
    "I hadn't made it as far in as I felt I must have - it looked deceptively easy, but I knew now the way the mud would pull you in and hold you close. No doubt it contributed to the infection in my leg."
    show wisp
    "But as I look around, something catches my eye - the same blue light. It was the size of an insect, but without any body visible amid its glow."
    "Once I see it, it slowly begins swaying despite the lack of breeze, turning towards the bulrushes which I can now see are rustling."
    "As I look, a figure stands from among the reeds, holding something in her arms and looking over her shoulder at me with a smile."
    hide wisp
    show alys neutral at rightish
    with easeinright
    show tierney neutral at leftish
    with easeinleft
    "The woman is strange - almost ethereal. She walks through the muck with an ease I envy, somehow managing to remain mostly clean as she approaches with a smile."
    "A part of me recognizes that I don’t feel as bothered as I should that she has apparently stayed near me while I slept. Despite myself, I find it almost a comfort to see such a fine face after the days I’ve had."
    a "Well good morning. You were looking a little touch and go, there - I’m glad your fever seems to have broken."
    "Concern furrows her brow, but I notice she had done nothing to clean or tend to wound on my leg while I was out. I’m not sure how I feel about the idea that she could have - though it seems hard to argue with the prospect of waking in less pain than this."
    "Amid the humid scent of gentle decay I smell something more bright, the smell of freshly cut plants, and a lesser pain I had forgotten pushes its way to the forefront of my mind with a growl from my stomach."
    show alys laugh at rightish
    "The woman laughs, not unkindly, and sits a few feet away from me on the slightly sodden ground with all the poise of a lady on a cushioned bench."
    a "Hungry?"
    t "...A bit."
    show alys neutral
    "I reply with a hint of embarrassment. In response, she tosses a bag towards me that I quickly recognize as my own. With a raised eyebrow, I pick it up, rummaging until I find the remains of my pemmican." 
    "Several of our packs had been torn apart by the boar, so I am glad for the food, no matter how tart."
    "No doubt she had taken at least a cursory look at my pack. As far as I could tell, nothing had been taken, but it was still unsettling. I don’t know who this woman is, or why she is here."
    "Looking at her, I can see that she is working at the tall grasses she has gathered, cracking open the stalks and peeling away the fibers from the pale heart of them. She seems indifferent to my presence, content to continue her task in silence."
    "Once I slake the worst of my hunger and drink to wash away the grease lingering in the back of my throat, I watch her for a moment. Since she doesn’t seem inclined to leave or speak, I suppose I should introduce myself."
    t "Thank you. My name is Tierney. I’ve had…a rough few days of it."
    "She glances up at me in acknowledgement and smiles."
    a "I suppose you must have. Tell me about it?"
    "A thought occurs to me, later than it should have. I don’t even know how long this woman has been traveling - I see no supplies with her - but I have to ask."
    show tierney raise
    t "First - have you seen anyone else through here? Two men?"
    show alys contemplates
    a "I fear there are few visitors out here."
    show tierney annoyed
    "I curse quietly. After a moment more, I decide to explain yesterday’s attack, and how I had ended up here; without the men who should have been with me and missing - I now realized - more than the supplies that had been lost in the scrum."
    scene bg black
    pause
    nvl clear
    show bg boar
    play music "nightmare.ogg" fadeout 1.0 fadein 1.0
    pause
    nvl_narr "The journey had been quiet until then. No bandits, no foul weather: just clear trails and clearer skies as we made our way to our job."
    nvl_narr "Then Markus saw the trees rubbed raw, and gestured towards the tracks near it."
    nvl_narr "I scanned the undergrowth, but visibility was low in the thickness of the brush. It shouldn't have been a problem; we weren't here as hunters, and the swine should have had no issue with us."
    nvl_narr "The snapping of branches was our only warning."
    nvl clear
    nvl_narr "It erupted from the thicket like a demon loosed, bristled mane and yellowed tusk. Though Markus carried a spear, it had served him more as a walking stick on the journey, and he barely managed to bring it to bear before the beast slammed into him. The boar moved forward even as it was gouged, slamming Markus into a tree with a sickening crunch."
    nvl_narr "It bought enough time for Jakob and I to unsheathe our swords and brace as it wheeled with a speed that belied its heft. Its hide reflected my blade like armor, and as it charged past pain exploded through my leg as a tusk caught me, the force of it knocking me to the ground."
    nvl_narr "Jakob was shouting, though I couldn't tell what he said. The boar's hooves kicked up clods of earth as it wheeled for another charge at me. I had raised to my feet as quickly as I could, and despite the agony I was able to move out of the way and strike the animal with a blade to the neck."
    nvl clear
    nvl_narr "Everything collapsed into pain and sound. The horrid shriek of the animal, arterial spray gushing like an endless font. Markus, the bone in his arm exposed to the air. Retreating like hunted animals, slashing and giving ground, not willing to stop even when it seemed that the beast was done with it."
    nvl_narr "We fled out of the trees towards the wetlands, unwilling to stay penned and unable to see in the dense foliage, praying the boar's bulk over the soggy ground would hinder it more than it did us. Blood soaked my trouser leg, but fear kept me moving in a blur of pain and determination."
    nvl_narr "When the exhaustion began to outweigh the need to keep moving, we found the driest and most stable place we could, tending to our wounds to the best of our ability. Jakob, the least injured, took first watch. And then..."
    nvl clear
    stop music fadeout 1.0 
    scene bg lake
    show alys neutral at rightish
    show tierney sad at leftish
    "I stop, shake my head."
    "She's paused from her work and is looking at me with a furrowed brow, a look of sympathy that tugs at my heart."
    a "And what do you expect has happened?"
    "There seemed to be a simple answer…"
    menu:
        "They abandoned me.":
            show tierney annoyed
            "It was the most obvious conclusion: while I was asleep, they had decided I was dead weight and left without me. Though I could remember all too well the gory remains of what was once Markus' arm, he could walk better than I." 
            "I tell the woman as much, trying to keep my voice dispassionate."
            t "No doubt they’re looking to claim my share of payment for the job in my absence. They may have planned as much already, the boar simply gave them the opportunity."
            show alys regret
            "She nods sympathetically, but looks thoughtful."
            a "Such things are all too common, I’m afraid…though it’s perhaps a strange bit of sentimentality to leave you with what supplies they did."
            t "Maybe they felt better if they could tell themselves I might yet live. Or the pack was too close, and they didn’t want to risk waking me."
            show alys neutral
            a "Even injured, doubtlessly you would make a fearsome opponent for them."
            "It seems she’s mocking me, but despite the amusement in her eyes I sense no contempt. I have little enough wish to start quarreling with a strange woman in the state I am in anyway, so I don’t push it."
            jump choice1

        "They went for help.":
            $ humanity += 1
            show tierney sad
            "Though it was a questionable decision, I have to assume that they had tried to go ahead for help. Adrenaline had kept me moving longer than it should have, but my reserves of energy had been depleted, and now demand repayment tenfold." 
            "Infection had set in and left me weak and feverish. I would not have been fit to travel, and waiting to nurse my wounds wouldn’t be wise in these wilds."
            t "They must have gone ahead. I know there is a village nearby, where we intended to refill our canteens - I assume they have gone for more supplies and possible assistance, and intend to return soon."
            "She watches me with a thoughtful look for a moment before she speaks."
            a "Odd to steal away in the middle of the night, and with so many of the supplies. You seem a reasonable woman; surely you wouldn’t have objected to their plan had they given it to you."
            t "If it even was night. It may well have been morning, and in the worst of my fever, I don’t know if I was lucid enough to have been reasoned with."
            jump choice1

    label choice1:
        "While we speak, I begin to wash the wound on my leg with water from my canteen, hissing through the pain. I suture it closed as best I can despite the awkward angle, and toss the soiled bandages to the side."
        t "Whatever the case, I am glad you are alright. The fens are not a place to be taken lightly."
        show tierney neutral
        "I almost laugh - with my wound fully visible to her, I am surprised she would describe me as being alright." 
        "I had half expected her to grow faint at the sight of it when I started, but she seems nonplussed, sometimes watching me with mild interest, but mostly focusing on her own work."
        "The woman is strange in many ways, and I wonder what has brought her here. I wouldn’t have thought to traverse even slightly as far as I have into the wetlands if we hadn’t been desperately fleeing a set of angry tusks."
        show tierney raise
        t "Oh? Are you well acquainted with the mire? Though it isn’t the most pleasant to trudge through, I have found it far more appealing than the woods. No offense, lady…?"
        a "Alys."
        play music "Alys01.ogg" fadeout 1.0 fadein 1.0
        "She seems wryly amused - by the title or my assumptions about the region?"
        show alys hand
        a "Stay for a while, and you may find that you prefer the forest, even with its boars."
        "Before I can argue, she shifts, moving slightly closer to me and examining part of the results of her work: the cores she had managed to pluck from their stems."
        a "I've heard said that if a lost person finds bulrushes, they have four of the five things they need for survival: water, food, shelter, and a source of heat. They only lack companionship."
        play sound "bulrush crunch.ogg" volume 0.5
        "She holds out a handful of the cores. By way of explanation, she takes one and bites into it with a faint crunch."

    menu: 
        "Accept":

            "Though the pemmican helped, it is nothing compared to the prospect of something fresh and green after a week of travel rations. I take the proffered bundle, examining them out of curiosity over suspicion." 
            "My father had done plenty of foraging of his own in addition to his garden of medicinal herbs, so while I have no memories of anyone ever eating a bulrush the thought doesn’t seem beyond the pale."
            "I gamely pick one and bite into it, pleasantly surprised by the easy crunch and mild taste. In the state I’m in, it’s a finer sunket than I could hope for."
            t "Thank you."
            show alys laugh
            "She flashes me a smile."
            a "A soldier with manners? What a rare breed you are."
            jump choice2
        
        "Turn down":
            "Whether more from a distrust of the strange woman or an unwillingness to eat grasses like a goat I’m not entirely sure, but I gesture my rejection. She shrugs, but I see her giving me an appraising look out of the corner of her eye."
            "She may think me an ungracious guest all she wishes: I, for one, am less than impressed with her hosting abilities, regardless of the setting."
            show tierney annoyed
            t "No need."
            show alys laugh
            a "I suppose I don't blame you. A soldier is wise not to trust everyone she meets."
            "There's a hint of a teasing tone in her voice."
            jump choice2
            
    label choice2:
        show tierney annoyed
        "I scrunch my nose in distaste."
        t "I'm no soldier."
        a "No? You seem rather well armed for a villager. A routier, perhaps? Or do I have a simple bandit on my threshold?"
        "A particularly defended villager may have a set of leathers, and my brigandine was beyond that. It was costly enough to deter robbers in search of an easy target - and to attract some who thought that might mean I carry a bigger purse."
        t "I have no great passion for war or gold…we were on our way for work as guards."
        t "A wedding hosted by a minor lord. I understand he expected the possibility of some…problem guests."
        a "The woes of the wealthy. Do such things happen often?"
        t "Some get too far in their cups. Nothing the house staff can't handle, really, but I understand it can be useful to make a show of it."
        show tierney raise
        show alys neutral
        t "My companions spoke of competing in the tourney. They've been trying to convince me to join them in the melee…"
        "Alys tilts her head."
        a "Melee? These weddings do seem rather dangerous."
        "Though I know plenty of people live lives far from any manor, I have traveled enough and seen enough peasant crowds to be surprised at someone not having taken advantage of the entertainment."
        "My wound cleaned and stitched and my mind drawn elsewhere, I lean forward and begin to tell her of what I had seen: dances and feasts, fireworks and sugar sculptures."


        scene bg night 
        show alys neutral at rightish:
            matrixcolor TintMatrix("#3e465e") * SaturationMatrix(0.5)
        show tierney neutral at leftish:
            matrixcolor TintMatrix("#3e465e") * SaturationMatrix(0.5)
        with dissolve
        stop ambient fadeout 1.0
        play ambient "Nighttime Ambience.ogg" fadeout 1.0 fadein 1.0
        "I hardly notice when the sky begins to turn dark. I must have been asleep longer than I realized."
        show tierney annoyed
        "I curse my own distraction. It feels exposed out on the fens; while I can see quite a distance, I would prefer a place with more cover when camping by myself."
        "And with that thought, something occurred to me."
        show tierney raise
        t "Are you… camping out here?"
        a "Mhmm."
        t "Without a tent?"
        show alys laugh
        a "Not when the stars are so lovely."
        "I'm not unfamiliar with sleeping on nothing but a bed roll, but despite her foraging skills, Alys doesn't quite seem the type for rough camping."
        "Despite her short hair, there's something almost delicate about her manner. I would expect to see her examining bolts of cloth for a new dress, not in the slough."
        "Already I can feel the air start to get colder, and I have more sleeves and layers than she."
        t "With the way the midges bite, I would rather have the tent."
        stop music fadeout 1.0 
        a "Have they been biting?"
        "She asks with a tone of mock innocence, and I realize that despite my expectations, I haven't swatted at a single bug today."
        scene bg evening
        with dissolve
        "Instead of the swarm like I saw the previous night, all I could see were those odd glow-worms, more visible now without the sun to compete with."
        "I watch them for a while, head tilted up, before glancing back at Alys with an eyebrow raised. She grins, says nothing."
        t "...I suppose I've slept in worse places."
        a "That's the spirit. The grass is rather soft as well, if you fancy."
        "I know she's messing with me, and I'm almost tempted to take the bait. But I still have so little energy, and I break into a yawn instead."
        a "I suppose I've been rather cruel, keeping you awake. It's...often not wise, to sleep out here. The weather can change so quickly."
        a "Some think themselves well prepared, only to be lost, caught in the cold rains."
        "I can picture it: stranded in the fog and the biting winds, with no landmarks visible on the expanse of hills."
        "A fire would be a comfort, but I don't trust my ability to find dry kindling in the dying light."
        "But the strange light of the glow-worms was some consolation."
        "Alys rests her chin on her hand, considering me."
        a "But I think you'll be alright."
        
        stop ambient fadeout 1.0
        scene bg lake
        with None
        play ambient "Daytime Ambience.ogg" fadeout 1.0 fadein 1.0
        play music "Wetlands01.ogg" fadeout 1.0 fadein 1.0
        show tierney neutral at center
        "I stand, testing my balance on my wounded leg. It stings in protest, but I've powered through worse. When I tentatively raise my heels, I'm nearly brought down by the pain, but I close my eyes and take a second to breathe through clenched teeth."
        show tierney neutral at leftish 
        with MoveTransition(0.35)
        show alys neutral at rightish
        with moveinright
        "As I open my eyes and lower my heels, rocking back and rolling my shoulders, I notice Alys watching me with an inscrutable expression I've begun to think is her norm." 
        show tierney smile
        "Once she notices me watching, I do my best to give a confident smile, but I fear it's less than convincing."
        "Sure enough, she shakes her head fondly."
        a "You could use some more rest. You're liable to open your stitches fighting through the muck."
        show tierney neutral
        t "A little walking won't hurt me. And I can't keep sitting here."
        "After I woke this morning, she told me she planned to leave, but would return after noon to check on me - but I insisted I'd follow her."
        "Apparently I've been fidgety enough that she realizes how irritating I'll be with nothing to do but sit."
        show alys hand
        a "Alright, you can come with me. But I'm not carrying you back."
        t "Are you planning on coming back to this exact spot? How would you know how to find it again?"  
        show alys laugh
        "She smiles and shakes her head, but gives me no reply."
        "Though I'm carrying little enough myself, it's strange to see she has no belongings to gather. It is as if she materialized out of the fog with nothing but the clothes on her back. I feel that if I look away, I may turn back to find she'd never been there."
        "But at the same time, she feels like the only thing real here in the quiet."
        "Wherever she's going, she needs no time to consider it. She moves without waiting to see if I follow."
        "I know I'm slower than I normally would be, but either it's more dire than I thought or she's faster than I could have anticipated. She walks with the ease of a woman on a clear path, while I clumsily pick my way along after her like a clumsy colt learning to walk."
        "But without the dire need to run, I adjust before long. The pain settles into a more ignorable ache, and I can appreciate my surroundings more." 
        show alys neutral
        "More signs of spring exist here than there had been in the woods; flowers bud and insects fly about the new shoots."
        "At times Alys stops, inspecting or collecting things as we go, but I pay her little mind. Small birds, none quite familiar to me, fly low overhead, hunting among the sedges. It's peaceful here, but the peace is soon troubled."
        "Alys gestures to the bottom of the hill, though as I lean to look she places a hand out, cautioning me not to fall."

        scene bg bone
        with fade
        pause

        "I take her warning more seriously when I see what she points at - bones, doubtlessly human. I've seen dead bodies, but the way it lays there, discarded and unacknowledged strikes me as deeply wrong."
        t "What is that? What happened?"
        a "He fell."
        "She speaks calmly, as though she's used to this."
        t "You saw it? You didn't help?"
        "She looks at me, and smiles sadly."
        a "The wetlands stretch a long way. Even I don't know everything that happens in it. And more happens than you think. People fall, the weather changes, the ground slips away beneath their feet. Everything here grows on death, more than most places." 

        menu:
            "He should have a burial":
                $ humanity += 1
                t "Horrible, to leave his body like this."
                a "Perhaps. But he has company. It would take too many people to drag out the remains of every soul who never left the fens."
                a "In some places, the bodies never rot. To attempt to pull them out would be to join them."
                "Spring has shown itself earlier here than in the woods, and this must be the cost: feeding on the decay of years."

                jump choice3
            "So it goes":
                t "Such is the way of it, I suppose."
                a "It always is."
                t "I feel that it should bother me more than it does."
                a "What good would it do? He's beyond any help now. Save your strength for the living."

                jump choice3

        label choice3:
        "We stand in silence for a moment, lost in our own thoughts."
        scene bg swamp
        show tierney neutral at leftish
        show alys neutral at rightish
        with dissolve
        stop music fadeout 1.0
        play music "Alys01.ogg" fadeout 1.0 fadein 1.0
        "Finally she turns away, and I follow her. Past the vast expanses of the peatland there are trees, though the swamp is still a far cry from the forest."
        "I don't mention my pain, but she notices it and calls for us to rest and catch our breath, though she doesn't seem the slightest bit tired."
        "The afternoon light filters green through the canopy overhead, casting dappled shadows across the fairly dry patch of ground where I gratefully sit."
        "She plucks some of the longer marsh grass, but this she weaves instead of eating. I see a glint as the bracelet circling her wrist catches the light as she works."
        "It's fashioned in the shape of a snake, curled above her hand, crude but carefully crafted bronze. I've seen her touch it absently at times as we spoke." 
        t "That's lovely."
        "I nod towards it."
        t "Did you make it?"
        show alys bashful
        "Her hands still their work for a moment. Then she smiles faintly, though it doesn't quite reach her eyes."
        a "No. It was a gift."
        "I wait, grasping my own grass and braiding it. I let silence draw more from her."
        show alys regret
        a "A child used to come through here. A lad from the village…"
        "She finally speaks, her fingertips brushing against the metal snake."
        a "He was crafty. He'd bring me little things he'd made - wreaths of flowers, a whittled branch. Only this lasted."
        show tierney raise
        t "A child? How did he end up here?"
        a "Ah, you know the way children are. Wandering where they shouldn't, no matter what their parents say."
        "There's fondness in her voice, with an edge of something else I can't quite read.."
        a "He was incorrigible. Fearless, even for his age. Felt that the moors called to him."
        "Alys laughs softly."
        a "He had so many questions, and when the answers he got didn't satisfy him, he came to me. He wanted to know everything, and I taught him what I could - what was safe to eat, what could be used to soothe a fever or a stomach ache."
        a "And he wanted to teach as much as he wanted to learn. He taught me games I'd forgotten existed, had me playing mill…"
        a "One day he brought me this, proud as the day is long. Told me he'd been angling for an apprenticeship with the silversmith, trying to learn his trade in secret. He'd made it from scraps and casting spills."
        t "Why a snake?"
        a "He was always quite taken with them. Collecting shed skins like jewels."
        "Her smile turns wry. I'm not sure if I want to ask my next question."
        t "What happened to him?"
        show alys contemplates
        a "He grew up. There are better things for a young man to do than traipse through the swamp."
        "She shrugs, a show of nonchalance, though I can sense her nostalgia."
        a "It's been…oh, years now. He doesn't look this way anymore."
        "I turn over her words in my mind, considering probing. But she has already returned to her weaving with a vengeance, movements precise and focused in a way that discourages my questions."
        show tierney neutral
        "For a moment, I think about questioning the necklace she wears, tucked close to her chest beneath her dress."
        "But after a while she speaks again, quietly enough that I nearly miss it."
        show alys regret
        a "It's the way of things. The living die, the young grow old, and it all begins again. Precious ephemera."
        "I lean against the trunk of a tree, abandoning my own crude project to watch her, and consider."
        stop music fadeout 1.0

        scene bg marsh
        with fade

        "As another day passes, the angry swelling on my leg has reduced, and I have stopped bleeding through my bandages. As interesting as this strange detour has been, I know it’s time for me to leave and figure out my next steps."
        "My last job was a bust: whatever happened to my companions, by now it was no longer worth trying to chase down an employer who doubtlessly no longer had any use for me."
        "Regardless of my long term goals, I long for a proper bath and change of clothes after four nights in the wetlands with my bloodied garments."
        "Alys doesn't seem surprised, but she has her own ideas on what I should do."

        show alys neutral at rightish
        with moveinright
        a "I'm simply saying it’d be a waste for you to end up dead in the muck."
        show tierney annoyed at leftish
        with moveinleft
        "I give her a withering look."
        show alys laugh
        a "Come, hunt with me. I'll be your harrier, and you can prove you're hale. Some game would do you some good, after the days of berries and leaves."
        show tierney raise
        "My eyebrows raise."
        t "You hunt so freely?"
        a "Let any lord who wishes feel free to challenge me."
        show alys neutral
        show tierney neutral
        play music "tierney01.ogg" fadeout 1.0 fadein 1.0
        "Alys moves through the peatlands like mist, each step precise and soundless. I feel clumsy next to her, boots sinking deeper into the soft earth than her sandaled feet ever seem to."
        "The morning fog still clings to the ground, blurring the boundaries between earth and bog."
        "I expect to find little apart from birds beyond what I can catch without a bow and arrow, but her confidence is founded: she gestures for me to stop, then points ahead with the faintest of whispers."
        a "There. See it, in the grass?"
        show tierney raise
        "I squint."
        show tierney smile
        t "A hare. Well spotted."
        a "Feeling limber? You can sit aside, if you'd like…"
        "I know she's baiting me, and I let her."
        t "And let you have all the fun? I think not."
        show tierney neutral
        "She circles around our prey, and I remain still, trusting her ability to move silently over mine. Now that I watch for it, I can see the hare snuffling among the peat, wary but still oblivious to our approach."
        "Alys gives me the slightest signal with her hand, and I understand her intent. She lunges forward, angled to drive the hare towards me."
        play audio ["<silence 2>", "slide fall into mud.ogg"]
        "I surge forward and strike with my knife, but my leg fails me. I slide into the muck, a stinging in my leg, but I laugh, and see Alys is laughing with me."
        "After a moment of fruitlessly wiping the mud from my trousers, we're off again, Alys leading us once more."
        play audio ["<silence 1>", "rabbit stab.ogg"]
        "The second attempt is more successful. As the hare tries to dash past me, I intercept it, and my blade strikes true behind the shoulders. Alys joins me as I finish it off and hold my prize aloft."
        show alys laugh
        "Alys laughs, the sound bright and wild in the morning air."
        a "Well struck!"
        "She claps me on the shoulder, her hand lingering."
        a "I'd say you've paid me back."
        show tierney smile
        "I realize I'm grinning too, flushed with the thrill of the hunt. I'd expected our efforts to be in vain."
        t "I'm starting to suspect you would have been perfectly capable on your own."
        show alys bashful
        "She shrugs innocently."
        a "Where's the fun in that?"
        show alys neutral
        show tierney neutral
        "I skin and gut the carcass, and once I am done Alys is in the distance, starting a fire at the place of her choosing. When I join her, I notice she's humming as she nurses the kindling, a tune I almost but don't quite recognize."
        t "Do you know every inch of these wetlands?"
        "She glances up at me, a look in her eyes that may be mischief or simply hunger."
        a "Not quite. But I could show you more, sometime. If you'd like."
        "I can sense what she's really asking, and it confirms something I'd begun to suspect: whoever - whatever - this woman is, she isn't inclined to leave here."
        "It should make me nervous. But I find myself nodding."
        show tierney smile
        t "I think I'd like that."
        stop music fadeout 1.0 

        scene bg village
        nvl_narr "It is a relief to be back among humanity, even as sparse as it is in the small village."
        nvl_narr "I have little left to me after the loss of our packs, but I must look pitiable, because when I enter the inn the owner offers me a chance to wash up in exchange for the hare pelt I carry."
        nvl_narr "Gratefully, I hand over the skin that has begun to stink, and scrub the past few days away."
        nvl_narr "Surprisingly, no one seems to know anything about my former companions. It seems hard to imagine they would simply skirt around the village, wounds and all."
        nvl_narr "No one else seems to find this strange. If anything, they remark on how lucky I was to get here safely."
        nvl_narr "Though my leg is healing, I know I won't be able to weather long days on the road yet, so I take what odd jobs I can."
        nvl clear
        nvl_narr "As the days pass, I notice that no one seems inclined to enter the wetlands. It is not mentioned, though I know there is plenty to be gained from it."
        nvl_narr "This early in the year, the bogs are flowering before anywhere else, and there are already berries to supplement last winter's stores."
        nvl_narr "So, despite the clear disapproval from anyone who hears of my plans, I venture out once more."
        nvl_narr "The hunting is good, and the townsfolk will use the peat I bring back, but I still get sidelong glances from them."
        nvl_narr "Often I am alone on my trips, but sometimes Alys will appear at my side as though she has come from the aether."
        nvl clear
        nvl_narr "I am glad to see her, to speak to someone without the undercurrent of suspicion, and to learn from her. I gather leaves for teas, roots for poultices."
        nvl_narr "She never returns with me, always with some quip if I ever ask. Wherever her home, she seems content to stay there, with no need for others."
        nvl_narr "Even as I become more useful, a local source of some medicinal plants they have been trading for from farther away, the chilliness grows as summer warms."
        nvl_narr "Whatever they feared, I was becoming the face of it. The more distant others became, the more often I was inclined to depart again."

        scene bg lake
        show tierney c neutral at leftish
        show alys neutral at rightish
        "While summer brings its heat, I am drawn to the wetlands still, despite its suffocating humidity."
        "Though some may find it oppressive, I've come to enjoy the way the marsh demands your awareness of it with each breath you take."
        "Those times I do encounter Alys are better; there must be something in her blood the midges dislike, and sitting next to her I am free from their biting myself."
        "We sit on a hill, enjoying the handful of apples I'd brought, and which she had examined like a craftsman inspecting jewels."
        play sound "apple knife carve.ogg" volume 0.5
        "With my knife she idly carves patterns into the skin of the last one; whorls, like water through the stream."
        "I enjoy bringing her these gifts perhaps even more than she likes receiving them."
        "Addicted to seeing the world through eyes capable of seeing wonder and beauty."
        "Glad that I can feel as though I provide something for her, even if she doesn't need it."
        "Beneath us, cranes leap and carouse gracefully in the water, unafraid as we watch."
        "Looking back, between the birds and Alys, there's a pang in my chest. As happy as I am to be here, I already feel the sadness of knowing I'll be leaving."
        t "I envy you. You have a place to belong. I feel out of place wherever I go, a ghost haunting my own life."
        show alys bashful
        a "You belong here. Or you could, if you wished."
        t "Here? In this place where so many die?"
        "The words come out harsher than I intended."
        "Perhaps it is fitting that she thinks so. Death seems to plague my steps no matter where they take me."
        "She looks down to the apple, considering."
        show alys regret
        a "Maybe they belonged here too, in their own way."
        "I think of all those who nature had interred here. What led them here, despite the danger?"
        "Had they felt the same pull that I do?"
        play sound "apple piece cut.ogg"
        "Alys cuts into the apple, finally, knife sinking into its tender flesh, and hands me the piece."
        "It's sweeter than it has any right to be."
        t "Thank you."
        show alys neutral
        "She smiles with a look that says she knows what I'm really thanking her for, then turns back to the birds."
        "Our shoulders nearly brush, and I wonder if she notices."

        scene bg talk
        play music "Conversation01.ogg" fadeout 1.0 fadein 1.0

        "Though none are more than civil to me anymore, one man has seemed more wary of me than any other." 
        "When I'm near he's tense, endeavoring not to be caught as he looks at me out of the corner of his eye."
        "I'm content to give him his space in turn: something foul twists in my chest when I think about him, though I'm aware I don't truly know the man, can lay no crime at his feet."
        "Something about me simply wants to reflect the judgment he casts on me."
        "Still, I will not go out of my way to avoid him, and the day comes when I contemplate a new weapon as I think of finally moving on." 
        "He's not working the metal when I approach, but managing his tools. I'm glad to catch him in a quiet moment."
        "The man was clearly torn between his distaste for me and his desire to prove something, either to me or himself."
        "Finally he seems to have come to some decision, and looks me in the eyes for the first time."
        m "You've seen her."
        "I know who he means, of course. I nod, but he is quiet for a while before I finally prompt him."
        t "...What happened?"
        "He furrows his brow, looks at me as though wondering my motivations."
        m "My mother - was gone. People said she'd fled, abandoned her duties. I grew restless, ranged further from the village. Found comfort in the hills."
        m "When they told me not to roam, I didn't listen. What did they know, speaking of my mother as they did? In the end they never stopped me."
        m "And when I found...her, I felt like the guardian of a knowledge everyone else was too foolish to recognize."
        "Did he not know her name, or could he simply not stand to speak it?"
        m "It went on for longer than it should have. Months. But I went once, without her, and -"
        "His voice falters."
        stop ambient fadeout 1.0
        m "I found her. My mother."
        m "When I spoke to her, she said she hadn't even known she was there. But she must have. Lying there - rotting. But not enough for me not to know her."
        m "I couldn't bring her body back. No one would have helped me. I wanted to take her bracelet, at least, but I - I couldn't touch her."
        m "I had trusted her. I thought she was just...lonely. Misunderstood. That only I could truly see her."
        m "But she knew. She knew, and she didn't even tell me."
        m "I ran. I wasn't sure she'd let me. I thought I'd die out there too, trapped like my mother, with her looking me in the eye and watching me die."
        m "I made it. I never went back."
        "Part of me feels compelled to defend alys, offer some justification for her. Violence seemed out of her character."
        "But to stand by and watch as someone drowned, like a child dispassionately observing a fly in a puddle?"
        "Well."
        t "...Thank you. For telling me."
        "I force the words out. He nods, curtly, turns away, no longer able to face me."
        "It's no matter; a new blade is the last thing on my mind now. Perhaps I still have work here."
        stop music fadeout 1.0

        scene bg hills
        play ambient "Daytime Ambience.ogg" fadeout 1.0 fadein 1.0
        "Part of me wonders if I will even be able to find her this time, or if I would wander alone once again."
        "Perhaps she would find me and lead me astray, so she wouldn't have to face this conversation."
        "Was I retreading old ground? Had others gone through these steps with her before?"
        "I could have left. Moved on entirely, forgotten all of the past months. But I feel a strange compulsion to see things through."
        show alys contemplates at rightish
        with easeinright
        "But I find her all too quickly, standing with the wind tugging at her dress."
        show alys neutral
        "She gives me a measured look, and I wonder if my thoughts show on my face, if she can read my feelings any better than I can."
        show tierney c neutral at leftish
        with easeinleft
        t "I don't feel that you've been entirely honest with me."
        a "Oh? And what lies have I told?"
        show tierney c mad
        t "Don't do that. It's unbecoming."
        show alys regret
        "She sighs, and looks away. I stand near her, looking at the same horizon where her gaze rests."
        t "If I had been wearing some shiny jewelry you wanted, would I be standing here?"
        a "Don't be crass. I took what I was left."
        t "You lead people to their lives or deaths on a whim. Like you led me."
        t "Tell me the truth of why you saved me. You owe me that much."
        show alys annoyed
        "Her gaze returns to me, and her measured neutrality is gone."
        a "I owe you nothing. Would you have me apologize for my nature?"
        t "I would have your honesty, for once."
        show alys hand
        a "Honesty? Very well. I didn't save your for anything, because I didn't save you."
        a "True, I didn't lead you to drown - but I found you bleeding and didn't raise a finger."
        show alys contemplates
        a "I meant to watch you die. That you didn't...is nothing to do with me, any more than if you had."
        "I notice her shoulders stiffen. She'd always spoken so casually about death, before, but now..."
        a "Your path has always been your own."
        "And now it takes me here, to this. No more inertia: a decision must be made."

        menu: 
            "I have to stop her":
                jump betray 
            "I believe she can be better" if (humanity == 2):
                jump redeem  
            "I just want to be with her" if (humanity == 0):
                jump join 
     
        label betray:

            "Ultimately, I know what it is I have to do."
            "As tempting as it is to take uncomplicated pleasure from her presence, I know she does not show this charming mask to all."
            "Her youthful face belies the long years she has spent terrorizing the locals, dragging people into the mire to suit her own whims."
            "No matter what she claims, she is no innocent."
            "I can no more let her continue than I could leave a viper among sleeping babes."
            "I endeavor to let none of this show on my face as I turn to her, my smile unforced despite everything."
            "I look into her eyes, reach out to cup the back of her neck. Were I not on such alert, I might not have noticed the way she leans imperceptibly into my touch."
            "I brush my thumb across the pleasant fuzz of her shorn hair at the base of her skull, and watch her watch me with a mischievous light in her eyes."
            scene bg kiss
            "It's no great task to let her pull me forward into a kiss that threatens to break my resolve. Despite living wilder than a grouse, her skin is deceptively soft, hands free of callouses as she reaches for my waist, my jaw."
            "My free hand raises as if of its own accord, lightly touching her collarbone, until, with a sudden strike -"
            "I grasp the pendant she wears beneath her dress, clutching it through the fabric, and clench my fist and shatter it with a sickening snap -"
            "The world lurches into darkness. There is a burning in the back of my eyes, and my nose stings with a sharp, sickening stench."
            scene bg strange
            with hpunch
            stop ambient fadeout 1.0
            play music "Betrayal02.ogg" fadeout 1.0 fadein 1.0
            "For a moment, I fail to register the scream, piercing as it is - shrill with despair and {i}rage{/i}."
            show alys annoyed at rightish
            a "What did you do??!"
            "She stumbles away from me, grasping at the pieces as though they could be brought together. It’s difficult to think, suddenly, with the crushing pressure around my head, threatening to split it apart."
            "With the malice in her eyes, I half expect her to lunge at me, but instead she takes a shuddering breath and sits on the ground. It seems that the best thing for me to do is to leave, now, before she comes to her senses."
            hide alys
            "Fighting not to sway as I walk, I turn to make my way out of the bog and toward the village, but my legs feel heavy, like trudging through water."
            "I walk. And walk until my legs begin to ache, the sun shifting the wrong direction in the sky above me, until I finally slow, dread heavy in my stomach."
            "I’ve returned to where I started."
            show tierney c mad at leftish
            with easeinleft
            t "Let me out."
            show alys annoyed at rightish
            with moveinright
            "She looks at me, eyes flinty, and smiles humorlessly."
            a "Oh, I haven’t done a thing. This is all you."
            "I had recognized the glimpse of the charm she wore on her neck, despite the way she kept it safely tucked away, knew it from my father’s notes. I had clearly been correct in assuming that this was what allowed her to roam."
            "I suppose I knew less than I thought. Despite my distrust of her, her words rang true. Her deceitful wisps were nowhere to be seen, and this didn’t match what I knew of her abilities, whatever she was."
            "She tosses the remains of her pendant at my feet. They are nothing to her now. Her voice, when she speaks, is bitter."
            show alys hand
            a "You must truly like me. You know, if you wanted to spend so much time with me, there were easier ways."
            "I stare at her with a sinking feeling. Whatever is happening isn't passing - won't pass. I'm as snared as she, and the thought makes me dizzy."
            a "I truly, {i}truly{/i} hope this was worth it for you."

            return
            

        label redeem:
            play music "Tierney01.ogg" fadeout 1.0 fadein 1.0
            show tierney c neutral
            "I take a moment to sort through all I want to say. It's hard to know where to begin."
            t "You know...I don't believe you're as callous as you pretend to be."
            "Her incredulous expression nearly makes me laugh, but I fight it down."
            t "How about this..."
            show alys neutral
            "Gently, I touch her arm and face her. She looks in my eyes searchingly, seeming almost - worried?"
            t "You've taught me a lot out here. Maybe...I should return the favor."
            "If she understands what I'm insinuating, she doesn't show it."
            "As much as I've grown to love it here, I don't know what I would become, alone here for years. Leaving may do her good."
            "If she even can."
            t "I think you'd enjoy the mountains."
            show alys bashful
            "It's clear she's trying to keep her face blank, but I see her eyebrow twitch. Instead of answering, she keeps watching me."
            "Is she expecting some trick? For me to change my mind? As if I hadn't thought long about my decision."
            "Despite everything, I want to believe she can be better."
            show alys contemplates
            a "And be...what? Some leashed pet you've tamed? Or do you just think I'd blend in as something mundane."
            "I know it's true. Even more than her physical appearance, she has a strange presence to her. But still..."
            "I pointedly glance at her ears and pretend to consider."
            show tierney c smile
            show alys neutral
            t "Hmm. Well, I think you'd look rather nice in a wimple."
            "She curls her lip, but I can tell she's amused, despite herself."
            t "There are other wildernesses. Perhaps we could find one that would suit us."
            "We stand there for what feels like forever, me patiently waiting for however long she needs, before she finally comes to some decision."
            "She takes a step away from me, and for a moment I feel unmoored, more than I thought I would have, but she doesn't move any further."
            "Instead, she reaches up, to the cord I've seen hang around her neck, pulling the pendant free from under her dress."
            "Reaching out, she offers it to me with a feigned air of nonchalance, as if it's just a paltry trinket."
            "I take it, not hesitating, but careful. The clay is warm from where it has lain against her skin."
            "Letting instinct guide me, I place it around my own neck. There's something achingly soft in her expression, and I place a hand on her shoulder."
            "Her eyes close, and then she reaches up, wraps her arms around me in a hug, burying her head in the crook of my neck with a huff."
            "I laugh quietly, and when she pulls back, I do what I'd been thinking about for weeks."
            scene bg kiss
            "Our lips meet, soft at first, then more hungry."
            "For a moment I let myself linger, and then I pull back, not wanting to be completely distracted."
            scene bg hills
            show tierney smile at leftish
            show alys bashful at rightish
            "Alys brushes my hand, our fingers twining together. I brush her knuckles with my thumb, and grin."
            a "It'll be difficult."
            t "Most worthwhile things are. Are you ready?"
            "The sun burns through the last of the mist. I kiss her forehead, and she smiles, small but sincere."
            show alys neutral
            a "No,"
            "She squeezes my hand and raises an eyebrow."
            a "But let's go anyway."

            return

        label join:
            play music "Alys01.ogg" fadeout 1.0 fadein 1.0
            t "I don't have your taste for cruelty."
            "A twinge of annoyance on her brow, but for now she does not speak."
            show tierney c sad
            t "I'm just...tired."
            "She places a hand on my elbow, and I lean into her touch."
            show alys regret
            a "I'm not as vicious as all that."
            "I snort, but there's no conviction in it."
            a "You don't need to worry about them. Not to hunt them, or save them."
            a "People will live or die as they are wont, no matter what you try."
            a "It's okay to be tired of trying."
            "And the truth is, I am. I hate how much the mundanity grates against me, confining, the petty distrust and betrayal."
            "I'm sick of scraping to richer men to make a living, biting my tongue and playing the role they want from me."
            "Especially when Alys looks at me like she sees every dark thought I've ever had and accepts them all."
            show tierney c neutral
            show alys neutral
            "She leans against me, and I lift my arm to make room, wrapping it around her and tucking her against me."
            "The weight of her feels like an anchor, keeping me steady."
            "It feels more right than anything has in longer than I can remember."
            t "And if I stay? What will I be?"
            a "Whatever you'd like. There's freedom here. If you want to play the hero, keep the marsh bloodless...well, you're welcome to try."
            t "But you'd rather I play the villain."
            a "I'd like you to be yourself, without carrying the weight of others' expectations."
            t "Even yours?"
            a "I expect only that you will continue to surprise me, whatever you do."
            "She twists in my embrace to face me, reaching up and ghosting her fingers along my jaw."
            "I smell the scent of wild herbs that linger on her hands, and feel like I can breathe."
            "When she pulls me to her, I lean to meet her."
            scene bg kiss
            "It's awkward, at first, but we soon adjust to each other."
            "She kisses softer than I would have expected, melting into my touch as I place my hand on her neck."
            "I can feel her pulse, the way it quickens, and I love that I can affect her like this."
            "Breaking the kiss, Alys puts a small distance between us."
            scene bg hills
            show tierney neutral at leftish
            show alys neutral at rightish    
            t "I'm not sure if I can be what you think I am."
            a "I'd still like to see you. Whatever you are."
            "The thought frightens me even as it thrills me. To be seen - to be seen by her."
            "What do I want her to see when she looks at me?"
            


        


    # This ends the game.

    return
