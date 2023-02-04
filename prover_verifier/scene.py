from manim import *


class ProverVerifierHashCheck(Scene):
    DODGER_BLUE = "#1E90FF"

    def exit_elements(self, elements):
        self.play(*[FadeOut(element) for element in elements])

    def scene_1(self):
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

        chat_bubble = ImageMobject("assets/dialogue/4.png")
        chat_bubble.move_to([2.5, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/5.png")
        chat_bubble.move_to([-3, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

    def trusted_setup_text(self):
        result = VGroup()
        text = Text("Trusted Setup", color=self.DODGER_BLUE, font_size=30)
        box = Rectangle(
            height=text.height + 0.5, width=text.width + 0.5,
            fill_opacity=0.5, stroke_color=self.DODGER_BLUE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def proving_algo_text(self):
        result = VGroup()
        text = Text("Proving Algorithm", color=self.DODGER_BLUE, font_size=30)
        box = Rectangle(
            height=text.height + 0.5, width=text.width + 0.5,
            fill_opacity=0.5, stroke_color=self.DODGER_BLUE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def scene_2(self):
        trusted_setup_text = self.trusted_setup_text()
        self.play(FadeIn(trusted_setup_text))

        lambda_text = Text('lambda', font_size=30, color=BLACK, weight=BOLD, slant=ITALIC)
        lambda_desc_text = Text('(A "very" secret value to be discarded later)', font_size=30, color=BLACK,
                                text2color={"discarded": RED})

        lambda_group = VGroup(lambda_text, lambda_desc_text).arrange(DOWN, buff=SMALL_BUFF)

        center = trusted_setup_text.get_center()[1] + trusted_setup_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 2, 0], end=[0, center, 0], color=BLACK)
        lambda_group = lambda_group.move_to(lambda_arrow, UP).shift(1 * UP)
        self.play(FadeIn(lambda_group), FadeIn(lambda_arrow))

        bottom_arrows_begin = [trusted_setup_text.get_center()[0],
                               trusted_setup_text.get_center()[1] - 0.65 * trusted_setup_text.height, 0]
        bottom_arrow_1_end = [bottom_arrows_begin[0] - 2, bottom_arrows_begin[1] - 2, 0]
        bottom_arrow_2_end = [bottom_arrows_begin[0] + 2, bottom_arrows_begin[1] - 2, 0]

        setup_bottom_arrow_1 = Arrow(start=bottom_arrows_begin, end=bottom_arrow_1_end, color=BLACK)
        setup_bottom_arrow_2 = Arrow(start=bottom_arrows_begin, end=bottom_arrow_2_end, color=BLACK)

        self.play(Create(setup_bottom_arrow_1), Create(setup_bottom_arrow_2))

        prover_key_text = Text("Prover Key (Pk)", color=BLACK, slant=ITALIC, font_size=25)
        prover_key_text.move_to(
            [bottom_arrow_1_end[0],
             bottom_arrow_1_end[1] - 0.5,
             0]
        )

        verifier_key_text = Text("Verifier Key (Vk)", color=BLACK, slant=ITALIC, font_size=25)
        verifier_key_text.move_to(
            [bottom_arrow_2_end[0],
             bottom_arrow_2_end[1] - 0.5,
             0]
        )

        self.play(Write(prover_key_text), Write(verifier_key_text))
        self.wait(2)

        line_begin = [bottom_arrow_1_end[0],
                      bottom_arrow_1_end[1] - 0.5,
                      0]
        line_end = [-5.2, 1.3, 0]
        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [bottom_arrow_2_end[0],
                      bottom_arrow_2_end[1] - 0.5,
                      0]
        line_end = [5.2, 1.8, 0]
        l2 = Line(line_begin, line_end, color=RED)

        self.play(
            FadeOut(trusted_setup_text), FadeOut(setup_bottom_arrow_1), FadeOut(setup_bottom_arrow_2),
            FadeOut(lambda_group), FadeOut(lambda_arrow),
            MoveAlongPath(prover_key_text, l1), MoveAlongPath(verifier_key_text, l2), rate_func=linear)
        self.wait(2)

    def scene_3(self):
        proving_algo_text = self.proving_algo_text()

        self.play(FadeIn(proving_algo_text))

        proving_key_text = Text('Pk, Secret Value (w), Hashed Value (x)', font_size=30,
                                t2w={"Pk": BOLD,
                                     "Secret Value (w)": BOLD,
                                     "Hashed Value (x)": BOLD},
                                color=BLACK, slant=ITALIC)

        center = proving_algo_text.get_center()[1] + proving_algo_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 2, 0], end=[0, center, 0], color=BLACK)
        proving_key_text = proving_key_text.move_to(lambda_arrow, UP).shift(1 * UP)
        self.play(FadeIn(proving_key_text), FadeIn(lambda_arrow))

        bottom_arrow_begin = [proving_algo_text.get_center()[0],
                              proving_algo_text.get_center()[1] - 0.65 * proving_algo_text.height, 0]
        bottom_arrow_1_end = [bottom_arrow_begin[0], bottom_arrow_begin[1] - 2, 0]

        bottom_arrow = Arrow(start=bottom_arrow_begin, end=bottom_arrow_1_end, color=BLACK)
        proof_text = Text("Proof", color=BLACK, slant=ITALIC, weight=BOLD, font_size=30)
        proof_text.move_to(bottom_arrow, DOWN).shift(0.6 * DOWN)

        self.play(Create(bottom_arrow), Write(proof_text))
        self.wait(2)
        self.play(FadeOut(proving_algo_text), FadeOut(lambda_arrow), FadeOut(proving_key_text),
                  FadeOut(bottom_arrow), FadeOut(proof_text))

        proving_arrow = Arrow(start=[-3, -1, 0], end=[3, -1, 0], color=BLACK)
        proof_text = Text("Proof", font_size=30, weight=BOLD, slant=ITALIC, color=self.DODGER_BLUE)
        proof_text.next_to(proving_arrow, UP)

        self.play(FadeIn(proving_arrow), FadeIn(proof_text))
        self.wait(2)
        self.play(FadeOut(proving_arrow), FadeOut(proof_text))

    def verification_algo_text(self):
        result = VGroup()
        text = Text("Verification Algorithm", color=self.DODGER_BLUE, font_size=30)
        box = Rectangle(
            height=text.height + 0.5, width=text.width + 0.5,
            fill_opacity=0.5, stroke_color=self.DODGER_BLUE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def scene_4(self):
        verification_algo_text = self.verification_algo_text()

        self.play(FadeIn(verification_algo_text))

        verification_input_text = Text('Vk, Hashed Value (x), Proof', font_size=30,
                                       t2w={"Vk": BOLD,
                                            "Proof": BOLD,
                                            "Hashed Value (x)": BOLD},
                                       color=BLACK, slant=ITALIC)

        center = verification_algo_text.get_center()[1] + verification_algo_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 2, 0], end=[0, center, 0], color=BLACK)
        verification_input_text = verification_input_text.move_to(lambda_arrow, UP).shift(1 * UP)
        self.play(FadeIn(verification_input_text), FadeIn(lambda_arrow))

        bottom_arrow_begin = [verification_algo_text.get_center()[0],
                              verification_algo_text.get_center()[1] - 0.65 * verification_algo_text.height, 0]
        bottom_arrow_1_end = [bottom_arrow_begin[0], bottom_arrow_begin[1] - 2, 0]

        bottom_arrow = Arrow(start=bottom_arrow_begin, end=bottom_arrow_1_end, color=BLACK)
        verification_op_text = Text("True / False", color=BLACK, slant=ITALIC, weight=BOLD, font_size=30)
        verification_op_text.move_to(bottom_arrow, DOWN).shift(0.6 * DOWN)

        self.play(Create(bottom_arrow), Write(verification_op_text))
        self.wait(2)

        self.play(FadeOut(verification_input_text), FadeOut(lambda_arrow), FadeOut(verification_input_text),
                  FadeOut(bottom_arrow), FadeOut(verification_op_text),
                  FadeOut(verification_algo_text))

    def intro(self):
        result = VGroup()
        understanding_zkp = Text("Understanding Zero Knowledge Proofs", font_size=50, color=self.DODGER_BLUE)
        box = Rectangle(
            height=understanding_zkp.height + 0.5, width=understanding_zkp.width + 0.5,
            fill_opacity=0.5, stroke_color=self.DODGER_BLUE
        )
        box2 = Rectangle(
            height=understanding_zkp.height + 1, width=understanding_zkp.width + 1,
            fill_opacity=0.5, stroke_color=self.DODGER_BLUE
        )
        understanding_zkp = understanding_zkp.move_to(box.get_center())
        result.add(box, box2, understanding_zkp)

        self.play(Create(box), Create(box2), Write(understanding_zkp))
        self.wait(2)
        self.exit_elements([understanding_zkp, box, box2])

    def outro(self):
        chat_bubble = ImageMobject("assets/dialogue/8.png")
        chat_bubble.move_to([1.8, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(4)

        self.play(FadeOut(chat_bubble))

    def construct(self):
        DODGER_BLUE = "#1E90FF"
        play_args = {"run_time": 4}
        self.camera.background_color = WHITE

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

        self.intro()

        self.add(prover_character, peggy_the_prover)

        verifier_character.move_to([5, -0.8, 0])
        victor_the_verifier.next_to(verifier_character, DOWN)

        self.add(verifier_character, victor_the_verifier)

        self.scene_1()

        self.scene_2()

        chat_bubble = ImageMobject("assets/dialogue/6.png")
        chat_bubble.move_to([-2.1, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        self.scene_3()

        chat_bubble = ImageMobject("assets/dialogue/7.png")
        chat_bubble.move_to([-2.1, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        self.scene_4()

        self.outro()

        self.exit_elements(self.mobjects)
        self.wait(1)
