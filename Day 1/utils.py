class Utils:
    def parse_values_from_text_file(path_to_file: str) -> list[str]:
        """Takes a path to a text file and returns the lines as a list of strings.

        Args:
            path_to_file (str): Absolute path to file.

        Returns:
            list[str]: Lines as a list of strings
        """
        with open(path_to_file) as file:
            lines = file.readlines()
            stripped_lines = [line.rstrip() for line in lines]
            return stripped_lines