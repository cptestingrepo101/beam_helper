import apache_beam as beam

class Pipeline_Helper(object):
    def printer(self):
        return beam.Map(print)
    
    def read_from_local(self,file_pattern,skip_header_lines,compression_type):
        return beam.io.ReadFromText(file_pattern=file_pattern,
                                    skip_header_lines=skip_header_lines, 
                                    compression_type=compression_type)

    def write_to_local(self, file_path_prefix, file_name_suffix, num_shards, compression_type):
        return beam.io.WriteToText(file_path_prefix=file_path_prefix,
                                    file_name_suffix=file_name_suffix,
                                    num_shards=num_shards,
                                    compression_type=compression_type)
    
    def read_from_bigquery(self, source_query):
        return beam.io.ReadFromBigQuery(
                    query=source_query,
                    use_standard_sql=True)
    
    def write_to_bigquery(self, output_table, create_disposition, write_disposition):
        return beam.io.WriteToBigQuery(
            table=output_table,
            create_disposition=create_disposition,
            write_disposition=write_disposition)

    def read_from_storage(self, file_pattern, skip_header_lines, compression_type):
        return beam.io.ReadFromText(file_pattern=file_pattern,
                                    skip_header_lines=skip_header_lines, 
                                    compression_type=compression_type)
    
    
    def write_to_storage(self, file_path_prefix, file_name_suffix, num_shards, compression_type):
        return beam.io.WriteToText(file_path_prefix=file_path_prefix, 
                                   file_name_suffix=file_name_suffix,
                                   num_shards=num_shards,
                                   compression_type=compression_type)

    def split_by_delimiter(self, delimiter):
        return beam.Map(lambda x: x.split(delimiter))
    
