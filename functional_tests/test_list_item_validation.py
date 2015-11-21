from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter no gthe empty input box

        # The home page refreshes, and there is an error message saying
        # tha list items cannot be blank

        # She tries again with some text for the item, which now works

        # Preversely, she now decideds to submt a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail("Write me!")
