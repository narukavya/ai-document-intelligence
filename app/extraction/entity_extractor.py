import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):

    doc = nlp(text)

    entities = {
        "PERSON": [],
        "ORG": [],
        "GPE": [],
        "DATE": [],
        "EMAIL": []
    }

    # Extract emails separately
    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    entities["EMAIL"] = list(set(emails))

    for ent in doc.ents:

        value = ent.text.strip()

        # Skip emails
        if "@" in value:
            continue

        # Skip very short values
        if len(value) < 3:
            continue

        # Skip common skill words from ORG
        unwanted_keywords = {
            "HTML",
            "CSS",
            "MLOps",
            "DevOps",
            "DataOps",
            "MS Power",
            "Logical Reasoning",
            "Interpersonal",
            "Bachelor",
            "Master",
            "Masters",
            "Computer Applications",
            "Skills",
            "Projects"
        }


        if ent.label_ == "ORG":

            if any(
                word.lower() in value.lower()
                for word in unwanted_keywords
            ):
                continue

        if ent.label_ in entities:

            entities[ent.label_].append(
                value
            )

    for key in entities:

        entities[key] = sorted(
            list(set(entities[key]))
        )

    return entities