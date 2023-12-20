# local imports
from content import generate_podcast_content
from soundfile import generate_audio_file
from thumbnail import generate_thumbnail

from api_management import is_xi_possible
from rss import fetch_article_content


def pipeline(
    topic: str,
    article_url: str,
    reference: str,
    with_thumbnail: bool = False,
    with_audio: bool = False,
) -> None:
    article_content = fetch_article_content(article_url=article_url)
    podcast_content = generate_podcast_content(
        reference=reference,
        source=article_content,
        topic=topic,
        article_endpoint=article_url,
    )

    if with_thumbnail:
        generate_thumbnail(
            prompt=podcast_content["thumbnail_prompt"],
            folder_name=podcast_content["folder_name"],
        )

    if with_audio:
        generate_audio_file(
            script=podcast_content["script"],
            folder_name=podcast_content["folder_name"],
        )

    print(f"Podcast {podcast_content['folder_name']} ready to be uploaded :)")
