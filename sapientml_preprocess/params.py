from typing import Union, Optional
from sapientml.params import Config


class PreprocessConfig(Config):
    use_word_list: Optional[Union[list[str], dict[str, list[str]]]] = None
    use_pos_list: Optional[list[str]] = ["名詞", "動詞", "助動詞", "形容詞", "副詞"]
    use_word_stemming: bool = True
