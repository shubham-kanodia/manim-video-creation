from manim import *
from types import SimpleNamespace


class ProverVerifierHashCheck(Scene):
    DODGER_BLUE = "#1E90FF"
    CREME = "#FF9966"

    PARAMETER_COLOR_1 = "#217C7E"
    PARAMETER_COLOR_2 = "#3399FF"
    PARAMETER_COLOR_3 = "#9A3334"

    def exit_elements(self, elements):
        self.play(*[FadeOut(element) for element in elements])

    def scene_1(self, retained_objects):
        chat_bubble = ImageMobject("assets/dialogue/1.png")
        chat_bubble.move_to([-2.3, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/2.png")
        chat_bubble.move_to([2, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/3.png")
        chat_bubble.move_to([-2.3, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/4.png")
        chat_bubble.move_to([2, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/dialogue/5.png")
        chat_bubble.move_to([-2.3, 2.2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2)

        self.play(FadeOut(chat_bubble))

        hashed_value_box = self.get_boxed_text("Hashed Value (x)", BLACK, BLACK, 18)
        secret_value_box = self.get_boxed_text("Secret Value (w)", BLACK, BLACK, 18)

        hashed_value_box.move_to([-5.5, 1.5, 0])
        secret_value_box_x = hashed_value_box.get_center()[0] + hashed_value_box.width + 0.3
        secret_value_box.move_to([secret_value_box_x, 1.5, 0])

        hashed_value_box_verifier = self.get_boxed_text("Hashed Value (x)", BLACK, BLACK, 18)
        hashed_value_box_verifier.move_to([4.5, 1.5, 0])

        self.play(Create(hashed_value_box), Create(secret_value_box), Create(hashed_value_box_verifier))

        retained_objects.hashed_value_box = hashed_value_box
        retained_objects.secret_value_box = secret_value_box
        retained_objects.hashed_value_box_verifier = hashed_value_box_verifier

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

    def scene_2(self, retained_objects):
        trusted_setup_text = self.trusted_setup_text()
        step_1_text = Text('STEP 1', font_size=30, color=self.CREME, weight=BOLD, font="sans-serif")
        lambda_text = self.get_boxed_text('lambda (A "very" secret value to be discarded later)', BLACK, BLACK, 18)
        # lambda_desc_text = Text(, font_size=18, color=BLACK,
        #                         text2color={"discarded": RED})

        lambda_group = VGroup(step_1_text, lambda_text).arrange(DOWN, buff=SMALL_BUFF)

        center = trusted_setup_text.get_center()[1] + trusted_setup_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 1.5, 0], end=[0, center, 0], color=BLACK)
        lambda_group = lambda_group.move_to(lambda_arrow, UP).shift(1.4 * UP)
        step_1_text.shift(0.2 * UP)
        self.play(FadeIn(trusted_setup_text), FadeIn(lambda_group), FadeIn(lambda_arrow))

        bottom_arrows_begin = [trusted_setup_text.get_center()[0],
                               trusted_setup_text.get_center()[1] - 0.65 * trusted_setup_text.height, 0]
        bottom_arrow_1_end = [bottom_arrows_begin[0] - 2, bottom_arrows_begin[1] - 2, 0]
        bottom_arrow_2_end = [bottom_arrows_begin[0] + 2, bottom_arrows_begin[1] - 2, 0]

        setup_bottom_arrow_1 = Arrow(start=bottom_arrows_begin, end=bottom_arrow_1_end, color=BLACK)
        setup_bottom_arrow_2 = Arrow(start=bottom_arrows_begin, end=bottom_arrow_2_end, color=BLACK)

        self.play(Create(setup_bottom_arrow_1), Create(setup_bottom_arrow_2))

        prover_key_text = self.get_boxed_text("Prover Key (Pk)", BLACK, BLACK, 18)
        prover_key_text.move_to(
            [bottom_arrow_1_end[0],
             bottom_arrow_1_end[1] - 0.5,
             0]
        )

        verifier_key_text = self.get_boxed_text("Verifier Key (Vk)", BLACK, BLACK, 18)
        verifier_key_text.move_to(
            [bottom_arrow_2_end[0],
             bottom_arrow_2_end[1] - 0.5,
             0]
        )

        self.play(Create(prover_key_text), Create(verifier_key_text))
        self.wait(2)

        line_begin = [bottom_arrow_1_end[0],
                      bottom_arrow_1_end[1] - 0.5,
                      0]
        line_end = [-4.4, 2.5, 0]
        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [bottom_arrow_2_end[0],
                      bottom_arrow_2_end[1] - 0.5,
                      0]
        line_end = [4.5, 2.5, 0]
        l2 = Line(line_begin, line_end, color=RED)

        self.play(
            FadeOut(trusted_setup_text), FadeOut(setup_bottom_arrow_1), FadeOut(setup_bottom_arrow_2),
            FadeOut(lambda_group), FadeOut(lambda_arrow),
            MoveAlongPath(prover_key_text, l1), MoveAlongPath(verifier_key_text, l2), rate_func=linear)
        self.wait(2)

        retained_objects.prover_key_text = prover_key_text
        retained_objects.verifier_key_text = verifier_key_text

    def scene_3(self, retained_objects):
        proving_algo_text = self.proving_algo_text()
        proving_algo_text.shift(DOWN)

        line_begin = [retained_objects.prover_key_text.get_center()[0],
                      retained_objects.prover_key_text.get_center()[1],
                      0]
        line_end = [0, 1.1, 0]
        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [retained_objects.hashed_value_box.get_center()[0],
                      retained_objects.hashed_value_box.get_center()[1],
                      0]
        line_end = [(-1 * retained_objects.hashed_value_box.width / 2) - 0.1, 2, 0]
        l2 = Line(line_begin, line_end, color=RED)

        line_begin = [retained_objects.secret_value_box.get_center()[0],
                      retained_objects.secret_value_box.get_center()[1],
                      0]
        line_end = [(retained_objects.secret_value_box.width / 2) + 0.1, 2, 0]
        l3 = Line(line_begin, line_end, color=RED)

        step_2_text = Text('STEP 2', font_size=30, color=self.CREME, weight=BOLD, font="sans-serif")
        step_2_text.move_to([
            0,
            retained_objects.secret_value_box.get_center()[1] + 1.3,
            0
        ])
        self.play(Create(step_2_text))

        self.play(
            MoveAlongPath(retained_objects.prover_key_text, l1),
            MoveAlongPath(retained_objects.hashed_value_box, l2),
            MoveAlongPath(retained_objects.secret_value_box, l3)
        )

        center = proving_algo_text.get_center()[1] + proving_algo_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 1.5, 0], end=[0, center, 0], color=BLACK)
        self.play(Create(proving_algo_text), Create(lambda_arrow))

        bottom_arrow_begin = [proving_algo_text.get_center()[0],
                              proving_algo_text.get_center()[1] - 0.5 * proving_algo_text.height, 0]
        bottom_arrow_1_end = [bottom_arrow_begin[0], bottom_arrow_begin[1] - 1.5, 0]

        bottom_arrow = Arrow(start=bottom_arrow_begin, end=bottom_arrow_1_end, color=BLACK)
        proof_text = self.get_boxed_text("Proof", BLACK, BLACK, 18)
        # proof_text = Text("Proof", color=BLACK, weight=BOLD, font_size=30)
        proof_text.move_to(bottom_arrow, DOWN).shift(0.8 * DOWN)

        self.play(Create(bottom_arrow), Create(proof_text))
        self.wait(2)

        line_begin = [retained_objects.verifier_key_text.get_center()[0],
                      retained_objects.verifier_key_text.get_center()[1],
                      0]
        line_end = [
            retained_objects.verifier_key_text.get_center()[0] + retained_objects.verifier_key_text.width / 2.3,
            retained_objects.verifier_key_text.get_center()[1],
            0]
        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [proof_text.get_center()[0],
                      proof_text.get_center()[1],
                      0]
        line_end = [
            retained_objects.verifier_key_text.get_center()[0] - 1,
            retained_objects.verifier_key_text.get_center()[1],
            0]
        l2 = Line(line_begin, line_end, color=RED)

        self.play(
            MoveAlongPath(retained_objects.verifier_key_text, l1),
            MoveAlongPath(proof_text, l2),
            FadeOut(step_2_text), FadeOut(proving_algo_text), FadeOut(lambda_arrow),
            FadeOut(bottom_arrow), FadeOut(retained_objects.hashed_value_box),
            FadeOut(retained_objects.secret_value_box),
            FadeOut(retained_objects.prover_key_text)
        )

        retained_objects.proof_text = proof_text

        self.wait(2)

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

    def get_boxed_text(self, text_content, text_color, box_colour, font_size):
        result = VGroup()
        text = Text(text_content, color=text_color, font_size=font_size)
        box = Rectangle(
            height=text.height + 0.5, width=text.width + 0.5,
            fill_opacity=0.5, stroke_color=box_colour
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def scene_4(self, retained_objects):
        verification_algo_text = self.verification_algo_text()
        verification_algo_text.shift(DOWN)

        to_move_x = retained_objects.hashed_value_box_verifier.get_center()[0]
        to_move_y = 0.3

        line_begin = [retained_objects.hashed_value_box_verifier.get_center()[0],
                      retained_objects.hashed_value_box_verifier.get_center()[1],
                      0]
        line_end = [0, retained_objects.hashed_value_box_verifier.get_center()[1] - to_move_y, 0]
        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [retained_objects.verifier_key_text.get_center()[0],
                      retained_objects.verifier_key_text.get_center()[1],
                      0]
        line_end = [
            retained_objects.verifier_key_text.get_center()[0] - to_move_x,
            retained_objects.verifier_key_text.get_center()[1] - to_move_y,
            0
        ]
        l2 = Line(line_begin, line_end, color=RED)

        line_begin = [retained_objects.proof_text.get_center()[0],
                      retained_objects.proof_text.get_center()[1],
                      0]
        line_end = [
            retained_objects.proof_text.get_center()[0] - to_move_x,
            retained_objects.proof_text.get_center()[1] - to_move_y,
            0
        ]
        l3 = Line(line_begin, line_end, color=RED)

        step_3_text = Text('STEP 3', font_size=30, color=self.CREME, weight=BOLD, font="sans-serif")
        step_3_text.move_to([
            0,
            retained_objects.proof_text.get_center()[1] + 0.5,
            0
        ])

        center = verification_algo_text.get_center()[1] + verification_algo_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 1.5, 0], end=[0, center, 0], color=BLACK)

        self.play(Create(step_3_text))

        self.play(
            Create(verification_algo_text), Create(lambda_arrow),
            MoveAlongPath(retained_objects.hashed_value_box_verifier, l1),
            MoveAlongPath(retained_objects.verifier_key_text, l2),
            MoveAlongPath(retained_objects.proof_text, l3)
        )

        bottom_arrow_begin = [verification_algo_text.get_center()[0],
                              verification_algo_text.get_center()[1] - 0.5 * verification_algo_text.height, 0]
        bottom_arrow_1_end = [bottom_arrow_begin[0], bottom_arrow_begin[1] - 1.5, 0]

        bottom_arrow = Arrow(start=bottom_arrow_begin, end=bottom_arrow_1_end, color=BLACK)
        verification_op_text = self.get_boxed_text("True / False", BLACK, BLACK, 18)
        verification_op_text.move_to(bottom_arrow, DOWN).shift(0.8 * DOWN)

        self.play(Create(bottom_arrow), Write(verification_op_text))
        self.wait(2)

        self.play(FadeOut(step_3_text),
                  FadeOut(retained_objects.proof_text),
                  FadeOut(retained_objects.verifier_key_text),
                  FadeOut(retained_objects.hashed_value_box_verifier),
                  FadeOut(lambda_arrow),
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

        prover_character = ImageMobject("assets/peggy.png")
        prover_character.height = 5
        prover_character.width = 3

        verifier_character = ImageMobject("assets/victor.png")
        verifier_character.height = 5
        verifier_character.width = 3

        prover_character.move_to([-5, -1.3, 0])

        retained_objects = SimpleNamespace()

        self.intro()

        self.add(prover_character)

        verifier_character.move_to([5, -1.3, 0])

        self.add(verifier_character)

        self.scene_1(retained_objects)

        self.scene_2(retained_objects)

        self.scene_3(retained_objects)

        self.scene_4(retained_objects)

        self.outro()

        self.exit_elements(self.mobjects)
        self.wait(1)
