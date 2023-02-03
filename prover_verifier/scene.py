from manim import *


class ProverVerifierHashCheck(Scene):
    def exit_elements(self, elements):
        self.play(*[FadeOut(element) for element in elements])

    def scene_1(self):
        pass

    def construct(self):
        DODGER_BLUE = "#1E90FF"
        play_args = {"run_time": 4}
        self.camera.background_color = WHITE

        understanding_zkp = Text("Understanding Zero Knowledge Proofs", font_size=40, color=DODGER_BLUE)
        self.play(FadeIn(understanding_zkp))
        self.wait(2)
        self.exit_elements([understanding_zkp])

        prover_character = ImageMobject("assets/prover.png")
        prover_character.height = 4
        prover_character.width = 2
        peggy_the_prover = Text("Peggy the Prover", font_size=26, color=DODGER_BLUE)

        verifier_character = ImageMobject("assets/verifier-new.png")
        verifier_character.height = 4.2
        verifier_character.width = 2.5
        victor_the_verifier = Text("Victor the Verifier", font_size=26, color=DODGER_BLUE)

        prover_character.move_to([-5, -1, 0])
        peggy_the_prover.next_to(prover_character, DOWN)

        self.add(prover_character, peggy_the_prover)

        verifier_character.move_to([5, -0.8, 0])
        victor_the_verifier.next_to(verifier_character, DOWN)

        self.add(verifier_character, victor_the_verifier)

        chat_bubble = ImageMobject("assets/dialogue/1.png")
        chat_bubble.move_to([-3, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/2.png")
        chat_bubble.move_to([2.5, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/3.png")
        chat_bubble.move_to([-3, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        self.exit_elements([prover_character, verifier_character, peggy_the_prover, victor_the_verifier])

        constraint_statement = Text("The program described in this problem can be written in pseudo code as...",
                                    font_size=30, color=BLACK)
        pseudo_code = Text("function C(x, w){\n\treturn hash(x) == w\n}",
                           font_size=30, color=DODGER_BLUE, weight=BOLD, font="Monospace")

        VGroup(constraint_statement, pseudo_code).arrange(DOWN, buff=1)
        self.play(Write(constraint_statement))
        self.play(Write(pseudo_code))

        self.wait(3)

        self.exit_elements([constraint_statement, pseudo_code])

        # Scene 3
        generator_intro_text = Text(
            'To solve this problem, \nA generator function (G) is used which takes in the program "C" and a secret value \nlambda which is not known to anybody to generate prover and verifier keys',
            font_size=30, color=BLACK, line_spacing=1.5)

        generator_function = Text(
            '(pk, vk) = G(C, lambda)',
            font_size=30, color=DODGER_BLUE)

        VGroup(generator_intro_text, generator_function).arrange(DOWN, buff=1)
        self.play(Write(generator_intro_text), **play_args)
        self.play(Write(generator_function), **play_args)

        self.exit_elements([generator_intro_text, generator_function])

        prover_intro_text = Text(
            'Using the proving function (P) which takes in the prover key, \nsecret value (w) and the hashed value (x), the prover generates a proof',
            font_size=30, color=BLACK, line_spacing=1.5)

        prover_function = Text(
            'Proof = P(pk, x, w)',
            font_size=30, color=DODGER_BLUE)

        VGroup(prover_intro_text, prover_function).arrange(DOWN, buff=1)

        self.play(Write(prover_intro_text), **play_args)
        self.play(Write(prover_function), **play_args)

        self.wait(3)

        self.exit_elements([prover_intro_text, prover_function])

        self.play(FadeIn(prover_character), FadeIn(verifier_character), FadeIn(peggy_the_prover), FadeIn(victor_the_verifier))

        proving_arrow = Arrow(start=[-3, -1, 0], end=[3, -1, 0], color=BLACK)
        proof_text = Text("Proof", font_size=30, color=DODGER_BLUE)
        proof_text.next_to(proving_arrow, UP)

        self.play(FadeIn(proving_arrow), FadeIn(proof_text))
        self.wait(2)

        self.exit_elements([peggy_the_prover, prover_character, victor_the_verifier, verifier_character, proving_arrow, proof_text])

        verifier_intro_text = Text(
            'Using the verifying function (V) which takes in the verification key, \nhashed value (x) and verification key the verifier is able to verify \nif the given proof is valid',
            font_size=30, color=BLACK, line_spacing=1.5)

        verifier_function = Text(
            'true/false = V(vk, x, proof)',
            font_size=30, color=DODGER_BLUE)

        VGroup(verifier_intro_text, verifier_function).arrange(DOWN, buff=1)

        self.play(Write(verifier_intro_text), **play_args)
        self.play(Write(verifier_function), **play_args)

        self.wait(3)

        self.exit_elements([verifier_intro_text, verifier_function])

        self.play(FadeIn(prover_character), FadeIn(verifier_character), FadeIn(peggy_the_prover),
                  FadeIn(victor_the_verifier))

        chat_bubble = ImageMobject("assets/dialogue/4.png")
        chat_bubble.move_to([2.5, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(4)

        self.exit_elements([prover_character, verifier_character, peggy_the_prover, victor_the_verifier, chat_bubble])