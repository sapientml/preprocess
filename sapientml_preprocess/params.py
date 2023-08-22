from typing import Optional, Union

from sapientml.params import Config


class PreprocessConfig(Config):
    use_pos_list: Optional[list[str]] = ["名詞", "動詞", "助動詞", "形容詞", "副詞"]
    use_word_stemming: bool = True
