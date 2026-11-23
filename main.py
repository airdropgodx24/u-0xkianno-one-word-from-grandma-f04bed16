"""One Word From Grandma — entry program.

Writes the single word a grandma would text about AI to /output/entry.txt.
The word is "whatchamacallit": the flustered, warm word a grandmother
types when she cannot name the gadget in front of her — which is exactly
what AI is to her. One word, no punctuation, no explanation. It beats the
obvious gadget words (thingamajig, doohickey, contraption) on freshness:
every one of those was already entered, while this, the longest and most
flustered of the family, was still free — and it reads the most like a
real text, typed in lowercase by someone giving up on the name mid-message.
"""

import os

WORD = "whatchamacallit"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
