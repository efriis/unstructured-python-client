"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class Files:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'files' }})
    



@dataclasses.dataclass
class PartitionParameters:
    chunking_strategy: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'chunking_strategy' }})
    r"""Use one of the supported strategies to chunk the returned elements. Currently supports: by_title"""
    combine_under_n_chars: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'combine_under_n_chars' }})
    r"""If chunking strategy is set, combine elements until a section reaches a length of n chars. Default: max_characters"""
    coordinates: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'coordinates' }})
    r"""If true, return coordinates for each element. Default: false"""
    encoding: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'encoding' }})
    r"""The encoding method used to decode the text input. Default: utf-8"""
    extract_image_block_types: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'extract_image_block_types' }})
    r"""The types of elements to extract, for use in extracting image blocks as base64 encoded data stored in metadata fields"""
    files: Optional[Files] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    r"""The file to extract"""
    gz_uncompressed_content_type: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'gz_uncompressed_content_type' }})
    r"""If file is gzipped, use this content type after unzipping"""
    hi_res_model_name: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'hi_res_model_name' }})
    r"""The name of the inference model used when strategy is hi_res"""
    include_orig_elements: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'include_orig_elements' }})
    r"""When True (the default), the elements used to form a chunk appear in `.metadata.orig_elements` for that chunk. Only applies when chunking is specified using the `chunking_strategy` argument."""
    include_page_breaks: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'include_page_breaks' }})
    r"""If True, the output will include page breaks if the filetype supports it. Default: false"""
    languages: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'languages' }})
    r"""The languages present in the document, for use in partitioning and/or OCR"""
    max_characters: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'max_characters' }})
    r"""If chunking strategy is set, cut off new sections after reaching a length of n chars (hard max). Default: 500"""
    multipage_sections: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'multipage_sections' }})
    r"""If chunking strategy is set, determines if sections can span multiple pages. Only applies to by_title chunking strategy.Default: true"""
    new_after_n_chars: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'new_after_n_chars' }})
    r"""If chunking strategy is set, cut off new sections after reaching a length of n chars (soft max). Default: max_characters (off)"""
    output_format: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'output_format' }})
    r"""The format of the response. Supported formats are application/json and text/csv. Default: application/json."""
    overlap: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'overlap' }})
    r"""A prefix of this many trailing characters from the prior text-split chunk is applied to second and later chunks formed from oversized elements by text-splitting. Default: None"""
    overlap_all: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'overlap_all' }})
    r"""When True, overlap is also applied to 'normal' chunks formed by combining whole elements. Use with caution as this can introduce noise into otherwise clean semantic units. Default: None"""
    pdf_infer_table_structure: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'pdf_infer_table_structure' }})
    r"""If True and strategy=hi_res, any Table Elements extracted from a PDF will include an additional metadata field, 'text_as_html', where the value (string) is a just a transformation of the data into an HTML <table>."""
    skip_infer_table_types: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'skip_infer_table_types' }})
    r"""The document types that you want to skip table extraction with. Default: ['pdf', 'jpg', 'png']"""
    split_pdf_page: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'split_pdf_page' }})
    r"""Should the pdf file be split at client. Ignored on backend."""
    strategy: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'strategy' }})
    r"""The strategy to use for partitioning PDF/image. Options are fast, hi_res, auto. Default: auto"""
    unique_element_ids: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'unique_element_ids' }})
    r"""When True, assign UUIDs to element IDs, which guarantees their uniqueness (useful when using them as primary keys in database). Otherwise a SHA-256 of element text is used. Default: False"""
    xml_keep_tags: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'xml_keep_tags' }})
    r"""If True, will retain the XML tags in the output. Otherwise it will simply extract the text from within the tags. Only applies to partition_xml."""
    

