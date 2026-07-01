# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: EventBoard
class TagManager:
    def __init__(self, event):
        self.event = event
        self.tags = {}  # {tag_name: count}

    def add_tag(self, name):
        if not name.strip(): return False
        self.tags[name] = self.tags.get(name, 0) + 1
        for item in [self.event.participants, self.event.tasks]:
            for obj in item:
                if 'tags' not in obj: obj['tags'] = []
                if name not in obj['tags']: obj['tags'].append(name)
        return True

    def remove_tag(self, name):
        if name not in self.tags or self.tags[name] == 0: return False
        self.tags[name] -= 1
        for item in [self.event.participants, self.event.tasks]:
            for obj in item:
                if 'tags' in obj and name in obj['tags']:
                    obj['tags'].remove(name)
        del self.tags[name]
        return True

    def get_tags(self):
        return list(self.tags.keys())
