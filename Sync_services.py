class SyncService:
    def __init__(self):
        self.records = []  # Store all records received from devices

    def onMessage(self, data: dict):
        if data['type'] == 'record':
            self.records.append(data)
            self.records.sort(key=lambda rec: rec['timestamp'])  # Ensure consistent order across devices
        elif data['type'] == 'probe':
            return self._create_update(data)
        else:
            # Unsupported message type
            raise ValueError(f"Unsupported message type: {data['type']}")

    def _create_update(self, probe_data):
        from_index = probe_data['from']
        update_data = self.records[from_index:]
        return {'type': 'update', 'from': from_index, 'data': update_data}
