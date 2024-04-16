from typing import Optional

def _parse_path(path: str) -> Optional[int]:
   split_path_ending = path.split('/')[-1]
   if split_path_ending:
      return int(split_path_ending)
   return None