from manim import *
from manim_fonts import *

from types import SimpleNamespace


class ProverVerifierHashCheck(Scene):
    DODGER_BLUE = "#1E90FF"
    CREME = "#FF9966"

    BACKGROUND_COLOR = "#212121"
    BOX_BACKGROUND = "#303030"
    BASE_FONT = "Roboto"

    def exit_elements(self, elements):
        self.play(*[FadeOut(element) for element in elements])

    def scene_1(self, retained_objects):
        secret_value_box = self.get_boxed_text("Secret Value (w)", WHITE, WHITE, 18)

        secret_value_box_x = retained_objects.prover_character.get_center()[0]
        secret_value_box.move_to([secret_value_box_x + 0.5, 1.5, 0])

        self.play(Create(secret_value_box))

        chat_bubble = ImageMobject("assets/revised/dialogue/1.png")
        chat_bubble.move_to([-0.8, 2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(2.4)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/revised/dialogue/2.png")
        chat_bubble.move_to([2, 2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(1.9)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/revised/dialogue/3.png")
        chat_bubble.move_to([-0.8, 2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(1.9)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/revised/dialogue/4.png")
        chat_bubble.move_to([2, 2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(1.9)

        self.play(FadeOut(chat_bubble))

        chat_bubble = ImageMobject("assets/revised/dialogue/5.png")
        chat_bubble.move_to([-0.8, 2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(1.9)

        self.play(FadeOut(chat_bubble))

        # hashed_value_box = self.get_boxed_text("Hashed Value (x)", WHITE, WHITE, 18)
        # secret_value_box = self.get_boxed_text("Secret Value (w)", WHITE, WHITE, 18)

        # Secret value final position - [-5.5, 1.5, 0]
        # hashed_value_box.move_to([-5.5, 1.5, 0])
        # secret_value_box_x = retained_objects.prover_character.get_center()[0]
        # secret_value_box.move_to([secret_value_box_x + 0.5, 1.5, 0])

        # hashed_value_box_verifier = self.get_boxed_text("Hashed Value (x)", WHITE, WHITE, 18)
        # hashed_value_box_verifier.move_to([4.5, 1.5, 0])

        # self.play(Create(secret_value_box))
        # self.wait(1)

        # retained_objects.hashed_value_box = hashed_value_box
        retained_objects.secret_value_box = secret_value_box
        # retained_objects.hashed_value_box_verifier = hashed_value_box_verifier

    def trusted_setup_text(self):
        result = VGroup()
        with RegisterFont(self.BASE_FONT) as fonts:
            text = Text("Trusted Setup", color=ORANGE, font_size=30, font=fonts[0])
        box = Rectangle(
            color=self.BACKGROUND_COLOR, height=text.height + 0.5, width=text.width + 0.5,
            stroke_color=ORANGE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def proving_algo_text(self):
        result = VGroup()
        with RegisterFont(self.BASE_FONT) as fonts:
            text = Text("Proving Algorithm", color=ORANGE, font_size=30, font=fonts[0])
        box = Rectangle(
            color=self.BACKGROUND_COLOR, height=text.height + 0.5, width=text.width + 0.5,
            stroke_color=ORANGE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def hash_fn_text(self):
        result = VGroup()
        with RegisterFont(self.BASE_FONT) as fonts:
            text = Text("Hash Function", color=ORANGE, font_size=18, font=fonts[0])
        box = Rectangle(
            color=self.BACKGROUND_COLOR, height=text.height + 0.5, width=text.width + 0.5,
            stroke_color=ORANGE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def scene_2(self, retained_objects):
        trusted_setup_text = self.trusted_setup_text()
        step_1_text = Text('STEP 1', font_size=30, color=self.CREME, weight=BOLD, font="sans-serif")
        lambda_text = self.get_boxed_text('lambda (A "very" secret value to be discarded later)', WHITE, WHITE, 18)

        lambda_group = VGroup(step_1_text, lambda_text).arrange(DOWN, buff=SMALL_BUFF)

        center = trusted_setup_text.get_center()[1] + trusted_setup_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 1.5, 0], end=[0, center, 0], color=WHITE)
        lambda_group = lambda_group.move_to(lambda_arrow, UP).shift(1.6 * UP)
        step_1_text.shift(0.2 * UP)
        self.play(FadeIn(step_1_text), FadeIn(trusted_setup_text))
        self.wait(4)

        self.play(FadeIn(lambda_text))
        self.wait(4)

        self.play(FadeIn(lambda_arrow))
        self.wait(2)

        bottom_arrows_begin = [trusted_setup_text.get_center()[0],
                               trusted_setup_text.get_center()[1] - 0.65 * trusted_setup_text.height, 0]
        bottom_arrow_1_end = [bottom_arrows_begin[0] - 2, bottom_arrows_begin[1] - 2, 0]
        bottom_arrow_2_end = [bottom_arrows_begin[0] + 2, bottom_arrows_begin[1] - 2, 0]

        setup_bottom_arrow_1 = Arrow(start=bottom_arrows_begin, end=bottom_arrow_1_end, color=WHITE)
        setup_bottom_arrow_2 = Arrow(start=bottom_arrows_begin, end=bottom_arrow_2_end, color=WHITE)

        self.play(Create(setup_bottom_arrow_1), Create(setup_bottom_arrow_2))

        prover_key_text = self.get_boxed_text("Prover Key (Pk)", WHITE, WHITE, 18)
        prover_key_text.move_to(
            [bottom_arrow_1_end[0],
             bottom_arrow_1_end[1] - 0.5,
             0]
        )

        verifier_key_text = self.get_boxed_text("Verifier Key (Vk)", WHITE, WHITE, 18)
        verifier_key_text.move_to(
            [bottom_arrow_2_end[0],
             bottom_arrow_2_end[1] - 0.5,
             0]
        )

        self.play(Create(prover_key_text), Create(verifier_key_text))
        self.wait(5)

        line_begin = [bottom_arrow_1_end[0],
                      bottom_arrow_1_end[1] - 0.5,
                      0]
        line_end = [-4.5, 2.5, 0]
        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [bottom_arrow_2_end[0],
                      bottom_arrow_2_end[1] - 0.5,
                      0]
        # line_end = [4.5, 2.5, 0]
        line_end = [4.5, 1.5, 0]
        l2 = Line(line_begin, line_end, color=RED)

        self.play(
            FadeOut(trusted_setup_text), FadeOut(setup_bottom_arrow_1), FadeOut(setup_bottom_arrow_2),
            FadeOut(lambda_group), FadeOut(lambda_arrow),
            MoveAlongPath(prover_key_text, l1), MoveAlongPath(verifier_key_text, l2), rate_func=linear)
        self.wait(2.5)

        retained_objects.prover_key_text = prover_key_text
        retained_objects.verifier_key_text = verifier_key_text

    def pre_scene_3(self, retained_objects):
        secret_value_box_2 = self.get_boxed_text("Secret Value (w)", WHITE, WHITE, 18)

        secret_value_box_2.move_to([
            retained_objects.secret_value_box.get_center()[0],
            retained_objects.secret_value_box.get_center()[1],
            0])

        self.add(secret_value_box_2)

        line_begin = [secret_value_box_2.get_center()[0],
                      secret_value_box_2.get_center()[1],
                      0]
        line_end = [0, 2, 0]

        l1 = Line(line_begin, line_end, color=RED)

        arrow = Arrow(
            start=[0, 2 - (secret_value_box_2.height / 2.0), 0],
            end=[0, 2 - (secret_value_box_2.height / 2.0) - 0.1 - 1.3, 0], color=WHITE)

        hash_function_text = self.get_boxed_text("Hash Function", ORANGE, ORANGE, 18)
        hash_function_text.move_to(
            [
                0,
                0.6 - (secret_value_box_2.height / 2.0) - 0.2,
                0
            ]
        )

        second_arrow = Arrow(
            start=[0, hash_function_text.get_center()[1] - (hash_function_text.height / 2.0), 0],
            end=[0, hash_function_text.get_center()[1] - (hash_function_text.height / 2.0) - 1.4, 0], color=WHITE)

        hashed_value_box = self.get_boxed_text("Hashed Value (x)", WHITE, WHITE, 18)
        hashed_value_box.move_to(
            [0,
             hash_function_text.get_center()[1] - (hash_function_text.height / 2.0) - 1.4 - 0.2,
             0]
        )
        self.wait(1)

        self.play(MoveAlongPath(secret_value_box_2, l1))
        self.play(FadeIn(arrow),
                  FadeIn(hash_function_text))
        self.wait(4)

        self.play(FadeIn(second_arrow),
                  FadeIn(hashed_value_box)
                  )

        self.wait(4)

        hashed_value_box_2 = self.get_boxed_text("Hashed Value (x)", WHITE, WHITE, 18)
        hashed_value_box_2.move_to(
            [hashed_value_box.get_center()[0],
             hashed_value_box.get_center()[1],
             0]
        )

        self.add(hashed_value_box_2)

        line_begin = [hashed_value_box.get_center()[0],
                      hashed_value_box.get_center()[1],
                      0]
        line_end = [4.5, 2.5, 0]

        l1 = Line(line_begin, line_end, color=RED)

        line_begin = [retained_objects.secret_value_box.get_center()[0],
                      retained_objects.secret_value_box.get_center()[1],
                      0]
        line_end = [-5.5, 1.5, 0]

        l3 = Line(line_begin, line_end, color=RED)

        line_begin = [hashed_value_box_2.get_center()[0],
                      hashed_value_box_2.get_center()[1],
                      0]
        line_end = [
            -5.5 + (retained_objects.secret_value_box.width / 2.0) + (hashed_value_box_2.width / 2.0) + 0.2,
            1.5,
            0]

        l2 = Line(line_begin, line_end, color=RED)
        self.play(
            MoveAlongPath(hashed_value_box, l1),
            MoveAlongPath(retained_objects.secret_value_box, l3),
            MoveAlongPath(hashed_value_box_2, l2),
            FadeOut(secret_value_box_2),
            FadeOut(arrow),
            FadeOut(second_arrow),
            FadeOut(hash_function_text)
        )

        retained_objects.hashed_value_box = hashed_value_box_2
        retained_objects.hashed_value_box_verifier = hashed_value_box
        self.wait(6)

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
        self.wait(3)

        self.play(
            MoveAlongPath(retained_objects.prover_key_text, l1),
            MoveAlongPath(retained_objects.hashed_value_box, l2),
            MoveAlongPath(retained_objects.secret_value_box, l3)
        )
        self.wait(7)

        center = proving_algo_text.get_center()[1] + proving_algo_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 1.5, 0], end=[0, center, 0], color=WHITE)
        self.play(Create(proving_algo_text), Create(lambda_arrow))
        self.wait(1)

        bottom_arrow_begin = [proving_algo_text.get_center()[0],
                              proving_algo_text.get_center()[1] - 0.5 * proving_algo_text.height, 0]
        bottom_arrow_1_end = [bottom_arrow_begin[0], bottom_arrow_begin[1] - 1.5, 0]

        bottom_arrow = Arrow(start=bottom_arrow_begin, end=bottom_arrow_1_end, color=WHITE)
        proof_text = self.get_boxed_text("Proof", WHITE, WHITE, 18)
        # proof_text = Text("Proof", color=WHITE, weight=BOLD, font_size=30)
        proof_text.move_to(bottom_arrow, DOWN).shift(0.8 * DOWN)

        self.play(Create(bottom_arrow), Create(proof_text))
        self.wait(1)

        proof_transfer_arrow = Arrow(
            start=[-3, -1, 0], end=[3, -1, 0], color=WHITE
        )

        self.play(
            FadeOut(step_2_text), FadeOut(proving_algo_text), FadeOut(lambda_arrow),
            FadeOut(bottom_arrow), FadeOut(retained_objects.hashed_value_box),
            FadeOut(retained_objects.secret_value_box),
            FadeOut(retained_objects.prover_key_text)
        )
        self.play(FadeIn(proof_transfer_arrow))

        line_begin = [proof_text.get_center()[0],
                      proof_text.get_center()[1],
                      0]
        line_end = [0, -0.2, 0]
        l1 = Line(line_begin, line_end, color=RED)

        self.play(MoveAlongPath(proof_text, l1))
        self.wait(1)

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
            FadeOut(proof_transfer_arrow),
            MoveAlongPath(retained_objects.verifier_key_text, l1),
            MoveAlongPath(proof_text, l2)
        )

        retained_objects.proof_text = proof_text
        self.wait(2)

    def verification_algo_text(self):
        result = VGroup()

        with RegisterFont(self.BASE_FONT) as fonts:
            text = Text("Verification Algorithm", color=ORANGE, font_size=30, font=fonts[0])

        box = Rectangle(
            color=self.BACKGROUND_COLOR, height=text.height + 0.5, width=text.width + 0.5,
            stroke_color=ORANGE
        )
        text = text.move_to(box.get_center())
        result.add(box, text)
        return result

    def get_boxed_text(self, text_content, text_color, box_colour, font_size):
        result = VGroup()

        with RegisterFont(self.BASE_FONT) as fonts:
            text = Text(text_content, color=text_color, font_size=font_size, font=fonts[0])

        box = Rectangle(
            color=self.BOX_BACKGROUND,
            height=text.height + 0.5, width=text.width + 0.5,
            stroke_color=box_colour
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
            retained_objects.hashed_value_box_verifier.get_center()[1] + 0.5,
            0
        ])

        center = verification_algo_text.get_center()[1] + verification_algo_text.height / 2
        lambda_arrow = Arrow(start=[0, center + 1.5, 0], end=[0, center, 0], color=WHITE)

        self.play(Create(step_3_text))

        self.play(MoveAlongPath(retained_objects.hashed_value_box_verifier, l1),
            MoveAlongPath(retained_objects.verifier_key_text, l2),
            MoveAlongPath(retained_objects.proof_text, l3))

        self.wait(3.5)

        self.play(
            Create(verification_algo_text), Create(lambda_arrow)
        )
        self.wait(1.5)

        bottom_arrow_begin = [verification_algo_text.get_center()[0],
                              verification_algo_text.get_center()[1] - 0.5 * verification_algo_text.height, 0]
        bottom_arrow_1_end = [bottom_arrow_begin[0], bottom_arrow_begin[1] - 1.5, 0]

        bottom_arrow = Arrow(start=bottom_arrow_begin, end=bottom_arrow_1_end, color=WHITE)
        verification_op_text = self.get_boxed_text("True / False", WHITE, WHITE, 18)
        verification_op_text.move_to(bottom_arrow, DOWN).shift(0.8 * DOWN)

        self.play(Create(bottom_arrow), Write(verification_op_text))
        self.wait(15)

        self.play(FadeOut(step_3_text),
                  FadeOut(retained_objects.proof_text),
                  FadeOut(retained_objects.verifier_key_text),
                  FadeOut(retained_objects.hashed_value_box_verifier),
                  FadeOut(lambda_arrow),
                  FadeOut(bottom_arrow), FadeOut(verification_op_text),
                  FadeOut(verification_algo_text))

    def intro(self):
        result = VGroup()

        with RegisterFont("Itim") as fonts:
            understanding_zkp = Text("Understanding Zero Knowledge Proofs", font_size=50, color=WHITE, font=fonts[0])

        box = Rectangle(
            color=self.BOX_BACKGROUND,
            height=understanding_zkp.height + 0.5, width=understanding_zkp.width + 0.5,
            stroke_color=ORANGE
        )
        understanding_zkp = understanding_zkp.move_to(box.get_center())
        result.add(box, understanding_zkp)

        self.play(Create(box), Write(understanding_zkp))
        self.wait(2)
        self.exit_elements([understanding_zkp, box])

    def outro(self):
        chat_bubble = ImageMobject("assets/revised/dialogue/6.png")
        chat_bubble.move_to([2, 2, 0])
        self.play(FadeIn(chat_bubble))
        self.wait(4)

        self.play(FadeOut(chat_bubble))

    def construct(self):
        DODGER_BLUE = "#1E90FF"
        play_args = {"run_time": 4}
        self.camera.background_color = self.BACKGROUND_COLOR

        prover_character = ImageMobject("assets/revised/Peggy.png")
        prover_character.height = 4
        prover_character.width = 12.0 / 5

        with RegisterFont(self.BASE_FONT) as fonts:
            peggy_text = Text("Peggy", font_size=20, color=WHITE, font=fonts[0], weight=BOLD)
            prover_text = Text("(Prover)", font_size=20, color=WHITE, font=fonts[0])

        prover_text_group = VGroup(peggy_text, prover_text).arrange(DOWN, buff=SMALL_BUFF)
        prover_text_group.move_to([-5.2, -3.2, 0])

        verifier_character = ImageMobject("assets/revised/Victor.png")
        verifier_character.height = 4
        verifier_character.width = 12.0 / 5

        with RegisterFont(self.BASE_FONT) as fonts:
            victor_text = Text("Victor", font_size=20, color=WHITE, font=fonts[0], weight=BOLD)
            verifier_text = Text("(Verifier)", font_size=20, color=WHITE, font=fonts[0])

        verifier_text_group = VGroup(victor_text, verifier_text).arrange(DOWN, buff=SMALL_BUFF)
        verifier_text_group.move_to([5, -3.1, 0])

        prover_character.move_to([-5, -0.8, 0])

        retained_objects = SimpleNamespace()
        retained_objects.prover_character = prover_character
        retained_objects.verifier_character = verifier_character

        self.intro()

        self.add(prover_character)
        self.add(prover_text_group)

        verifier_character.move_to([5, -0.8, 0])

        self.add(verifier_character)
        self.add(verifier_text_group)

        self.scene_1(retained_objects)

        self.scene_2(retained_objects)

        self.pre_scene_3(retained_objects)
        self.scene_3(retained_objects)

        self.scene_4(retained_objects)

        self.outro()

        self.exit_elements(self.mobjects)
        self.wait(1)
